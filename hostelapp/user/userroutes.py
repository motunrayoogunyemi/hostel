from flask import render_template,url_for,session

#import the blueprint's instance
from . import userobj

@userobj.route('/')
def home(): 
    return "Welcome to Home Page"

@userobj.route('/about-me/life')
def about(): 
    return render_template('about.html')