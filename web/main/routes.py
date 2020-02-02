from flask import Blueprint,render_template,request
from web import app
main=Blueprint('main',__name__)

@main.route('/')
def home():
    return 'Hello World'
