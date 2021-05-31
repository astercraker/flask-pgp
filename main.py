from re import T
from flask import Flask, render_template, abort, request
import os
from model import db, Post, Key
import random, threading, webbrowser
from flask_cachebuster import CacheBuster
from flask_gnupg import GnuPG
from datetime import datetime
import datedelta

gpg = GnuPG()
app = Flask(__name__)
settings_module = os.getenv('APP_SETTINGS_MODULE') if os.getenv('APP_SETTINGS_MODULE') else 'config.DevelopmentConfig'

config = { 'extensions': ['.js', '.css', '.csv'], 'hash_size': 5 }
cache_buster = CacheBuster(config=config)
cache_buster.init_app(app)


app.config.from_object(settings_module)
gpg.init_app(app)
db.init_app(app)

@app.route("/")
def welcome():
    keys_list = []
    keys_dict = gpg.list_keys()
    for key in keys_dict:
        print(key)
        key_obj = Key(key)
        keys_list.append(key_obj)
    print("keys List: ", keys_list)
    return render_template("admin_llaves.html", message="", keys=keys_list)

@app.route("/admin_llaves")
def admin_llaves():
    keys_list = []
    keys_dict = gpg.list_keys(True)
    for key in keys_dict:
        key_obj = Key(key)
        print(key)
        keys_list.append(key_obj)
    print("keys List: ", keys_list)
    return render_template("admin_llaves.html", message="", keys=keys_list)

@app.route("/generar_llave", methods=['GET', 'POST'])
def generar_llave():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contrasenia = request.form.get('password')
        local_dt = datetime.now() + datedelta.datedelta(years=2)
        input_data = gpg.gen_key_input(key_type="RSA", key_length=2048, name_real=nombre, name_email=correo, subkey_type= 'RSA',subkey_length=2048,expire_date=local_dt.strftime("%Y-%m-%d"), passphrase=contrasenia)
        key = gpg.gen_key(input_data)
        print("input", key)
    return render_template("generar_llave.html")

@app.route("/importar_llave", methods=['GET', 'POST'])
def importar_llave():
    if request.method == 'POST':
        text_key = request.form.get('text-key')
        import_result = gpg.import_keys(text_key)
        print(import_result)
    return render_template("import_keys.html")

if __name__ == '__main__':
    app.run(debug=True) 
