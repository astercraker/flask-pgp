from os import name
from typing import Dict
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)
    pass
class Key(db.Model):
    __tablename__ = 'keys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, nullable=False)
    keyID = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    expires = db.Column(db.DateTime, nullable=True)
    def __init__(self, my_dict) -> Dict:
        super().__init__()
        self.keyID = my_dict["keyid"]
        listName =  my_dict["uids"][0].split("<")
        self.name = listName[0]
        self.correo = listName[1].replace(">", "")
        ts = int(my_dict["date"])
        self.date = datetime.utcfromtimestamp(ts)
        print("---------------",type(my_dict["expires"]))
        print(type(my_dict["expires"]))
        if my_dict["expires"]:
            ts = int(my_dict["expires"])
            self.expires = datetime.utcfromtimestamp(ts)