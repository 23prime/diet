import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Weights(db.Model):
    __tablename__ = 'weights'
    date = db.Column(db.String(5), primary_key = True)
    weight = db.Column(db.String(4))

    def __repr__(self):
        return "Weights({}, {})".format(self.date, self.weight)
