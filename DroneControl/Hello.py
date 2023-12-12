from flask import Flask, redirect, url_for,render_template,request
from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
import socket
# import socketio
# from flask_socketio import SocketIO, emit
HOST = "172.168.0.46"
PORT = 5999
app=Flask(__name__,static_folder='static', static_url_path='/static')
vehicle=None
s=None
conn=None
# socketio = SocketIO(app)
def initialize_socket():
   global s,HOST,PORT,conn
   print("hi",s,HOST,PORT)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   print(s)
   s.bind((HOST,PORT))
   print("waiting")
   time.sleep(5)

   s.listen()
   conn,addr=s.accept()
   print("connection established")

def dataTrans():
   global conn
   print(s)
   time.sleep(10)
   while s:
      data=conn.recv(1024)
      print(f"Recieved from client {data}")
      start_time = time.time()
      with open("data.txt", "rb") as fi:
            data = fi.read(1024)
            while data:
               conn.send(data)
               data = fi.read(1024)
      conn.send(b"EOF")
      end_time = time.time()
      print("File sent successfully")
      rtt = end_time - start_time
      print(f"Round-trip time: {rtt} seconds")
      print(f"{(1000/1024)/rtt} mbps")
      return (1000/1024)/rtt
def listEBBports():
    # Find and return a list of all EiBotBoard units
    # connected via USB port.
    try:
        from serial.tools.list_ports import comports
    except ImportError:
        print("can't get",ImportError)
        return None
    if comports:
        com_ports_list = list(comports())
        ebb_ports_list = []
        for port in com_ports_list:
            port_has_ebb = False
            if port[1].startswith("EiBotBoard"):
                port_has_ebb = True
            elif port[2].startswith("USB VID:PID=04D8:FD92"):
                port_has_ebb = True
            if port_has_ebb:
                ebb_ports_list.append(port)
        if ebb_ports_list:
            return ebb_ports_list 
# def handle_update_data(data):
#    emit('update_data_response', {'alt': data['alt'], 'dir': data['dir'], 'speed': data['speed'], 'connectionSpeed': data['connectionSpeed']})
@app.route('/')
def start():
   return render_template('About_page.html')
@app.route("/main1")
def goto_page():
   return render_template('Goto.html',lat=vehicle.location.global_relative_frame.lat,long=vehicle.location.global_relative_frame.lon)
@app.route("/connect",methods=['POST'])
def connect_vehicle():
   if request.method=='POST':
      # user = request.form['nm']
      s1=listEBBports()
      print("s1: ",s1)
      s="tcp:127.0.0.1:5760"
      print(s)
      try:
         global vehicle 
         vehicle= connect1(s)
         print(vehicle)
         print("Waiting Socket Connection")
         initialize_socket()
         print("Socket Initialized")
      except Exception as e:
         print(f"Failed to connect: {str(e)}")

      vehicle.wait_ready('autopilot_version')
      print(vehicle.location.global_relative_frame)
      if(int(vehicle.location.global_relative_frame.alt)==0):
         return render_template('takeoff.html',lat=vehicle.location.global_relative_frame.lat,long=vehicle.location.global_relative_frame.lon)
      else:
         return render_template('Goto.html',lat=vehicle.location.global_relative_frame.lat,long=vehicle.location.global_relative_frame.lon)
def connect1(s):
   vehicle = connect(s, wait_ready=True)
   print("\nConnecting to vehicle on: %s" % s)
   vehicle.wait_ready('autopilot_version')
   return vehicle

@app.route('/main',methods=['POST'])
def arm_and_takeoff():
   global vehicle
   if(int(vehicle.location.global_relative_frame.alt)==0):
      if request.method == 'POST':
         alt = request.form['alt']
         
         x=dataTrans()
         x=20
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

            # socketio.emit('update_data_response', {'alt': alt, 'dir': vehicle.heading, 'speed': vehicle.airspeed, 'connectionSpeed': x})
            # socketio.emit('update_data_response', {'alt': vehicle.location.global_relative_frame.alt,'dir': vehicle.heading,'speed': vehicle.airspeed,'connectionSpeed': 20})  # Assuming 20 for x, change as needed
            print(" Altitude: ", vehicle.location.global_relative_frame.alt,vehicle.location.global_relative_frame)
            # Break and return from function just below target altitude.
            
            if vehicle.location.global_relative_frame.alt >=int(alt) -0.05:
               print("Reached target altitude")
               break
            time.sleep(1)
            # render_template("index.html",alt=vehicle.location.global_relative_frame.alt,dir=vehicle.heading,speed=vehicle.airspeed,connectionSpeed=x)
         print(vehicle.battery,vehicle.heading)
         # render_template("index.html",alt=vehicle.location.global_relative_frame.alt,dir=vehicle.heading,speed=vehicle.airspeed,connectionSpeed=x)
         return render_template("index.html",alt=vehicle.location.global_relative_frame.alt,dir=vehicle.heading,speed=vehicle.airspeed,connectionSpeed=x)
   else:
      long=float(request.form['long'])
      lat=float(request.form['lat'])
      alt=float(request.form['alt'])
      point1 = LocationGlobalRelative(lat,long,alt)
      point1.yaw=0.0
      if(vehicle.mode!="GUIDED"):
         vehicle.mode = VehicleMode("GUIDED")
      vehicle.armed = True
      while not vehicle.armed:
         print(" Waiting for arming...")
         time.sleep(1)
      
      print("goto!")
      vehicle.simple_goto(point1)
      while True:
         print(" Altitude: ", vehicle.location.global_relative_frame.alt,int(vehicle.location.global_relative_frame.lat*1000) ,int(lat*1000), int(vehicle.location.global_relative_frame.lon*1000) ,int(1000*long))
      # Break and return from function just below target altitude.
         if int(vehicle.location.global_relative_frame.lat*1000) ==int(lat*1000) and int(vehicle.location.global_relative_frame.lon*1000) ==int(1000*long):
            print("Reached location",vehicle.location.global_relative_frame)
            break
         time.sleep(20)
      x=dataTrans()
      return render_template("index.html",alt=vehicle.location.global_relative_frame.alt,dir=vehicle.heading,speed=vehicle.airspeed,connectionSpeed=x)
@app.route('/return_to_home')
def return_to_home():
   global vehicle
   try:
      vehicle.mode = VehicleMode("RTL")
      while not vehicle.mode.name == 'RTL':
         pass
      return render_template("takeoff.html", message="Returning to Home (RTL)...")
   except Exception as e:
      # Handle any exceptions that might occur during the process
      return render_template("index.html", error=f"Error: {str(e)}")
@app.route('/Land')
def land():
   global vehicle
   try:
      vehicle.mode = VehicleMode("LAND")
      while not vehicle.mode.name == 'LAND':
         pass
      return render_template("takeoff.html", message="Returning to Home (RTL)...")
   except Exception as e:
      # Handle any exceptions that might occur during the process
      return render_template("index.html", error=f"Error: {str(e)}")

if __name__=='__main__':
   app.debug = True
     # Initialize the socket before running the Flask app
   # socketio.run(app, debug=True) #Charan update
   app.run(debug=True)   # this works
   s.close()
   

