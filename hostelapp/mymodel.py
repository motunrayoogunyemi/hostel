import datetime

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Property(db.Model):
    prop_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    prop_contact = db.Column(db.String(100),nullable=False)
    prop_phone = db.Column(db.String(20),nullable=False)
    prop_filename = db.Column(db.String(255),nullable=False)
    prop_price = db.Column(db.Float(200),nullable=True)
    prop_name = db.Column(db.String(200),nullable=False)
    prop_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

class Merchants(db.Model):
    mer_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    mer_username = db.Column(db.String(100),nullable=False)
    mer_pwd = db.Column(db.String(255),nullable=False)
    mer_dateadded = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    