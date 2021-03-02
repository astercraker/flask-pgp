from flask import Flask, render_template, abort

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html", message="Mensage desde Jinga")


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card)
    except IndexError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
