from flask import Flask, redirect, url_for,render_template,request
from dronekit import connect, VehicleMode
import time
app=Flask(__name__,static_folder='static', static_url_path='/static')
vehicle=None
@app.route('/')
def start():
   return render_template('frontend.html')
@app.route('/main')
def success():
    return render_template('main.html')
@app.route("/connect",methods=['POST'])
def connect_vehicle():
   if request.method=='POST':
      # user = request.form['nm']
      s="tcp:127.0.0.1:5760"
      print(s)
      try:
         global vehicle 
         vehicle= connect1(s)
         print(vehicle)
      except Exception as e:
         print(f"Failed to connect: {str(e)}")

      vehicle.wait_ready('autopilot_version')
      return render_template('main.html')
def connect1(s):
   vehicle = connect(s, wait_ready=True)
   print("\nConnecting to vehicle on: %s" % s)
   vehicle.wait_ready('autopilot_version')
   return vehicle

@app.route('/main',methods=['POST'])
def arm_and_takeoff():
  if request.method == 'POST':
      alt = request.form['alt']
      global vehicle
      # connection_string = 'udp:127.0.0.1:14550'
      print(" Waiting for vehicle to initialise... %s "% vehicle)
      while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

      print("Arming motors")
    # Copter should arm in GUIDED mode
      vehicle.mode = VehicleMode("GUIDED")
      vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
      while not vehicle.armed:
         print(" Waiting for arming...")
         time.sleep(1)

      print("Taking off!")
      vehicle.simple_takeoff(alt)
      while True:

         print(" Altitude: ", vehicle.location.global_relative_frame.alt,vehicle.location.global_relative_frame)
         # Break and return from function just below target altitude.
         if vehicle.location.global_relative_frame.alt >=int(alt) -0.05:
               print("Reached target altitude")
               break
         time.sleep(1)
      return render_template("index.html",alt=alt,dir=270,speed=20)
# @app.route('/takeoff')
# def arm_and_takeoff():
#   if request.method == 'POST':
#       alt = request.form['alt']
#       global vehicle
#       # connection_string = 'udp:127.0.0.1:14550'
#       print(" Waiting for vehicle to initialise... %s "% vehicle)
#       while not vehicle.is_armable:
#         print(" Waiting for vehicle to initialise...")
#         time.sleep(1)

#       print("Arming motors")
#     # Copter should arm in GUIDED mode
#       vehicle.mode = VehicleMode("GUIDED")
#       vehicle.armed = True

#     # Confirm vehicle armed before attempting to take off
#       while not vehicle.armed:
#          print(" Waiting for arming...")
#          time.sleep(1)

#       print("Taking off!")
#       vehicle.simple_takeoff(alt)
#       while True:

#          print(" Altitude: ", vehicle.location.global_relative_frame.alt,vehicle.location.global_relative_frame)
#          # Break and return from function just below target altitude.
#          if vehicle.location.global_relative_frame.alt >=int(alt) -0.05:
#                print("Reached target altitude")
#                break
#          time.sleep(1)
#       return render_template("index.html",alt=alt,dir=270,speed=20)
# def indicators(alt,dir,speed):
#    return redirect(url_for('HelloWorld',name = name))
if __name__=='__main__':
    app.debug = True
    app.run(debug=True)
   


# from flask import Flask
# app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# if __name__ == '__main__':
#    app.run(debug = True)