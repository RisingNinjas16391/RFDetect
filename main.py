from flask import Flask, escape
from flask import render_template, request, Response

import RPi.GPIO as GPIO


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
  
if __name__ == "__main__":
   print("Start")
   app.run(host='0.0.0.0',port=5010)  
