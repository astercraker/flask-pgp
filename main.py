from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

#from model import db

app = Flask(__name__)
settings_module = os.getenv('APP_SETTINGS_MODULE')

app.config.from_object(settings_module)
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)

@app.route("/")
def welcome():
    post = Post.query.order_by(Post.fecha.desc()).all()
    return render_template("welcome.html", message="Mensaje desde Jinja!", post=post)


@app.route("/card/<int:index>")
def card_view(index):
    try:
        return render_template("card.html", card=card)
    except IndexError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
