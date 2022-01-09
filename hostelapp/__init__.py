#This file will import all the things we need in this package so that it #will be assessible to any module in the package, any module can import as #from thispackage import xx '''

from flask import Flask

#from flask_wtf.csrf import CSRFProtect

from hostelapp.admin import adminobj
from hostelapp.user import userobj
from hostelapp.api import apiobj

def create_app():
    app=Flask(__name__,instance_relative_config=True)
    from hostelapp import config #config within package folder
    app.config.from_object(config.LiveConfig)
    app.config.from_pyfile('config.py') #loads config from instance folder
    from hostelapp.mymodel import db
    db.init_app(app)
    app.register_blueprint(adminobj)
    app.register_blueprint(userobj)
    app.register_blueprint(apiobj)
    return app
from hostelapp import forms
from hostelapp import mymodel