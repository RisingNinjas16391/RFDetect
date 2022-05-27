from flask import Flask, escape
from flask import render_template, request, Response

from Motor import Motor
import json

PINS = [0, 1]
app = Flask(__name__)

agitator = Motor(PINS, True)

#TODO: add sensor class with multiprocessing to count balls

sensor1 = None
sensor2 = None

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/countballs')
    def sensor():
        # add sensor polling; maybe sensor.getcount?
        return "nothing for now"

@app.route('/centeragitator')
def agitate():
    if 'stop' in request.args and request.args['stop'].lower() = "true":
        agitator.set_power(0)
        return "stopped motor"
    else:
        agitator.set_power(100)
        return "started motor"
  
if __name__ == "__main__":
   print("Start")
   app.run(host='0.0.0.0',port=5010)  
