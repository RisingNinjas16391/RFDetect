from flask import Flask, escape
from flask import render_template, request, Response

import RPi.GPIO as GPIO
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/centeragitator')
def centera():
    //need to create function
    return "oops"
  
if __name__ == "__main__":
   print("Start")
   app.run(host='0.0.0.0',port=5010)  
