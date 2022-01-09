from flask import render_template,url_for,session


#import the blueprint's instance
from . import adminobj


@adminobj.route('/')
def home(): 
    return "Welcome to Home Page"

@adminobj.route('/about-me')
def about(): 
    return render_template('about.html')