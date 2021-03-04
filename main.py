from flask import Flask, render_template, abort
import os
from model import db, Post

app = Flask(__name__)
settings_module = os.getenv('APP_SETTINGS_MODULE') if os.getenv('APP_SETTINGS_MODULE') else 'config.DevelopmentConfig'

app.config.from_object(settings_module)
db.init_app(app)

@app.route("/")
def welcome():
    new_post = Post(
        titulo="Hola 3",
        texto="Texto"
    )
    db.session.add_all([new_post])
    db.session.commit()
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
