# # from dronekit import connect

# # Connect to the Vehicle (in this case a UDP endpoint)
# # vehicle = connect('127.0.0.1:14550', wait_ready=True)
# # # Get an instance of the API endpoint
# # api = local_connect()
# # # Get the connected vehicle (currently only one vehicle can be returned).
# # vehicle = api.get_vehicles()[0]


# # my_argument = int(local_arguments[0])


# # # LOCATION

# # print "Global Location: %s" % vehicle.location.global_frame
# # print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
# # print "Local Location: %s" % vehicle.location.local_frame


# #Takeoff and movement commands
# # DKPY2.0 instead provides Vehicle.simple_takeoff and Vehicle.simple_goto. These are the same as the old methods except that simple_goto allows you to optionally set the default target groundspeed and airspeed.

# # Vehicle.airspeed and Vehicle.groundspeed are now settable values. Call these to set the default target speed used when moving with Vehicle.simple_goto (or other position-based movement commands).

# # Home location
# #  Vehicle.home_location attribute.

# # Observing attribute changes
# # The DroneKit-Python 1.x observer function vehicle.add_attribute_observer has been replaced by Vehicle.add_attribute_listener() or Vehicle.on_attribute() in DKYP2.x, and Vehicle.remove_attribute_observer has been repaced by remove_attribute_listener().


# # Intercepting MAVLink Messages
# # DroneKit-Python 1.x used Vehicle.set_mavlink_callback() and Vehicle.unset_mavlink_callback to set/unset a callback function that was invoked for every single mavlink message.

# # In DKPY2 this has been replaced by the Vehicle.on_message() decorator, which allows you to specify a callback function that will be invoked for a single message (or all messages, by specifying the message name as the wildcard string ‘*’).

# # New attributes
# # In addition to the home_location, a few more attributes have been added, including: Vehicle.system_status, Vehicle.heading, Vehicle.mount_status, Vehicle.ekf_ok, Vehicle.is_armable, Vehicle.last_heartbeat




# print("Start simulator (SITL)")
# import dronekit_sitl
# sitl = dronekit_sitl.start_default()
# connection_string = sitl.connection_string()

# # Import DroneKit-Python
# from dronekit import connect, VehicleMode

# # Connect to the Vehicle.
# print("Connecting to vehicle on: %s" % (connection_string,))
# vehicle = connect(connection_string, wait_ready=True)

# # Get some vehicle attributes (state)
# print("Get some vehicle attribute values:")
# print (" GPS: %s" % vehicle.gps_0)
# print (" Battery: %s" % vehicle.battery)
# print (" Last Heartbeat: %s" % vehicle.last_heartbeat)
# print (" Is Armable?: %s" % vehicle.is_armable)
# print (" System status: %s" % vehicle.system_status.state)
# print (" Mode: %s" % vehicle.mode.name )   # settable

# # Close vehicle object before exiting script
# vehicle.close()

# # Shut down simulator
# sitl.stop()
# print("Completed")









# # Connect to the Vehicle (in this case a UDP endpoint)
# # vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)
# # Windows computer connected to the vehicle using a 3DR Telemetry Radio on COM14	com14 (also set baud=57600)





# from __future__ import print_function
# from dronekit import connect, VehicleMode
# import time

# #Set up option parsing to get connection string
# import argparse  
# parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
# parser.add_argument('--connect', 
#                    help="vehicle connection target string. If not specified, SITL automatically started and used.")
# args = parser.parse_args()

# connection_string = args.connect
# sitl = None


# #Start SITL if no connection string specified
# import dronekit_sitl
# if not connection_string:
    
#     sitl = dronekit_sitl.start_default()
#     connection_string = sitl.connection_string()


# # Connect to the Vehicle. 
# #   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
# print("\nConnecting to vehicle on: %s" % connection_string)
# vehicle = connect(connection_string, wait_ready=True)

# vehicle.wait_ready('autopilot_version')

# # Get all vehicle attributes (state)
# print("\nGet all vehicle attribute values:")
# print(" Autopilot Firmware version: %s" % vehicle.version)
# print("   Major version number: %s" % vehicle.version.major)
# print("   Minor version number: %s" % vehicle.version.minor)
# print("   Patch version number: %s" % vehicle.version.patch)
# print("   Release type: %s" % vehicle.version.release_type())
# print("   Release version: %s" % vehicle.version.release_version())
# print("   Stable release?: %s" % vehicle.version.is_stable())
# print(" Autopilot capabilities")
# print("   Supports MISSION_FLOAT message type: %s" % vehicle.capabilities.mission_float)
# print("   Supports PARAM_FLOAT message type: %s" % vehicle.capabilities.param_float)
# print("   Supports MISSION_INT message type: %s" % vehicle.capabilities.mission_int)
# print("   Supports COMMAND_INT message type: %s" % vehicle.capabilities.command_int)
# print("   Supports PARAM_UNION message type: %s" % vehicle.capabilities.param_union)
# print("   Supports ftp for file transfers: %s" % vehicle.capabilities.ftp)
# print("   Supports commanding attitude offboard: %s" % vehicle.capabilities.set_attitude_target)
# print("   Supports commanding position and velocity targets in local NED frame: %s" % vehicle.capabilities.set_attitude_target_local_ned)
# print("   Supports set position + velocity targets in global scaled integers: %s" % vehicle.capabilities.set_altitude_target_global_int)
# print("   Supports terrain protocol / data handling: %s" % vehicle.capabilities.terrain)
# print("   Supports direct actuator control: %s" % vehicle.capabilities.set_actuator_target)
# print("   Supports the flight termination command: %s" % vehicle.capabilities.flight_termination)
# print("   Supports mission_float message type: %s" % vehicle.capabilities.mission_float)
# print("   Supports onboard compass calibration: %s" % vehicle.capabilities.compass_calibration)
# print(" Global Location: %s" % vehicle.location.global_frame)
# print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
# print(" Local Location: %s" % vehicle.location.local_frame)
# print(" Attitude: %s" % vehicle.attitude)
# print(" Velocity: %s" % vehicle.velocity)
# print(" GPS: %s" % vehicle.gps_0)
# print(" Gimbal status: %s" % vehicle.gimbal)
# print(" Battery: %s" % vehicle.battery)
# print(" EKF OK?: %s" % vehicle.ekf_ok)
# print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
# print(" Rangefinder: %s" % vehicle.rangefinder)
# print(" Rangefinder distance: %s" % vehicle.rangefinder.distance)
# print(" Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
# print(" Heading: %s" % vehicle.heading)
# print(" Is Armable?: %s" % vehicle.is_armable)
# print(" System status: %s" % vehicle.system_status.state)
# print(" Groundspeed: %s" % vehicle.groundspeed)    # settable
# print(" Airspeed: %s" % vehicle.airspeed)    # settable
# print(" Mode: %s" % vehicle.mode.name)    # settable
# print(" Armed: %s" % vehicle.armed)    # settable



# # Get Vehicle Home location - will be `None` until first set by autopilot
# while not vehicle.home_location:
#     cmds = vehicle.commands
#     cmds.download()
#     cmds.wait_ready()
#     if not vehicle.home_location:
#         print(" Waiting for home location ...")
# # We have a home location, so print it!        
# print("\n Home location: %s" % vehicle.home_location)


# # Set vehicle home_location, mode, and armed attributes (the only settable attributes)

# print("\nSet new home location")
# # Home location must be within 50km of EKF home location (or setting will fail silently)
# # In this case, just set value to current location with an easily recognisable altitude (222)
# my_location_alt = vehicle.location.global_frame
# my_location_alt.alt = 222.0
# vehicle.home_location = my_location_alt
# print(" New Home Location (from attribute - altitude should be 222): %s" % vehicle.home_location)

# #Confirm current value on vehicle by re-downloading commands
# cmds = vehicle.commands
# cmds.download()
# cmds.wait_ready()
# print(" New Home Location (from vehicle - altitude should be 222): %s" % vehicle.home_location)


# print("\nSet Vehicle.mode = GUIDED (currently: %s)" % vehicle.mode.name) 
# vehicle.mode = VehicleMode("GUIDED")
# while not vehicle.mode.name=='GUIDED':  #Wait until mode has changed
#     print(" Waiting for mode change ...")
#     time.sleep(1)


# # Check that vehicle is armable
# while not vehicle.is_armable:
#     print(" Waiting for vehicle to initialise...")
#     time.sleep(1)
    # If required, you can provide additional information about initialisation
    # using `vehicle.gps_0.fix_type` and `vehicle.mode.name`.
    
#print "\nSet Vehicle.armed=True (currently: %s)" % vehicle.armed 
#vehicle.armed = True
#while not vehicle.armed:
#    print " Waiting for arming..."
#    time.sleep(1)
#print " Vehicle is armed: %s" % vehicle.armed 


# Add and remove and attribute callbacks

#Define callback for `vehicle.attitude` observer
# last_attitude_cache = None
# def attitude_callback(self, attr_name, value):
#     # `attr_name` - the observed attribute (used if callback is used for multiple attributes)
#     # `self` - the associated vehicle object (used if a callback is different for multiple vehicles)
#     # `value` is the updated attribute value.
#     global last_attitude_cache
#     # Only publish when value changes
#     if value!=last_attitude_cache:
#         print(" CALLBACK: Attitude changed to", value)
#         last_attitude_cache=value

# print("\nAdd `attitude` attribute callback/observer on `vehicle`")     
# vehicle.add_attribute_listener('attitude', attitude_callback)

# print(" Wait 2s so callback invoked before observer removed")
# time.sleep(2)

# print(" Remove Vehicle.attitude observer")    
# # Remove observer added with `add_attribute_listener()` specifying the attribute and callback function
# vehicle.remove_attribute_listener('attitude', attitude_callback)


        
# # Add mode attribute callback using decorator (callbacks added this way cannot be removed).
# print("\nAdd `mode` attribute callback/observer using decorator") 
# @vehicle.on_attribute('mode')   
# def decorated_mode_callback(self, attr_name, value):
#     # `attr_name` is the observed attribute (used if callback is used for multiple attributes)
#     # `attr_name` - the observed attribute (used if callback is used for multiple attributes)
#     # `value` is the updated attribute value.
#     print(" CALLBACK: Mode changed to", value)

# print(" Set mode=STABILIZE (currently: %s) and wait for callback" % vehicle.mode.name) 
# vehicle.mode = VehicleMode("STABILIZE")

# print(" Wait 2s so callback invoked before moving to next example")
# time.sleep(2)

# print("\n Attempt to remove observer added with `on_attribute` decorator (should fail)") 
# try:
#     vehicle.remove_attribute_listener('mode', decorated_mode_callback)
# except:
#     print(" Exception: Cannot remove observer added using decorator")



 
# # Demonstrate getting callback on any attribute change
# def wildcard_callback(self, attr_name, value):
#     print(" CALLBACK: (%s): %s" % (attr_name,value))

# print("\nAdd attribute callback detecting ANY attribute change")     
# vehicle.add_attribute_listener('*', wildcard_callback)


# print(" Wait 1s so callback invoked before observer removed")
# time.sleep(1)

# print(" Remove Vehicle attribute observer")    
# # Remove observer added with `add_attribute_listener()`
# vehicle.remove_attribute_listener('*', wildcard_callback)
    


# # Get/Set Vehicle Parameters
# print("\nRead and write parameters")
# print(" Read vehicle param 'THR_MIN': %s" % vehicle.parameters['THR_MIN'])

# print(" Write vehicle param 'THR_MIN' : 10")
# vehicle.parameters['THR_MIN']=10
# print(" Read new value of param 'THR_MIN': %s" % vehicle.parameters['THR_MIN'])


# print("\nPrint all parameters (iterate `vehicle.parameters`):")
# for key, value in vehicle.parameters.iteritems():
#     print(" Key:%s Value:%s" % (key,value))
    

# print("\nCreate parameter observer using decorator")
# # Parameter string is case-insensitive
# # Value is cached (listeners are only updated on change)
# # Observer added using decorator can't be removed.
 
# @vehicle.parameters.on_attribute('THR_MIN')  
# def decorated_thr_min_callback(self, attr_name, value):
#     print(" PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))


# print("Write vehicle param 'THR_MIN' : 20 (and wait for callback)")
# vehicle.parameters['THR_MIN']=20
# for x in range(1,5):
#     #Callbacks may not be updated for a few seconds
#     if vehicle.parameters['THR_MIN']==20:
#         break
#     time.sleep(1)


# #Callback function for "any" parameter
# print("\nCreate (removable) observer for any parameter using wildcard string")
# def any_parameter_callback(self, attr_name, value):
#     print(" ANY PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))

# #Add observer for the vehicle's any/all parameters parameter (defined using wildcard string ``'*'``)
# vehicle.parameters.add_attribute_listener('*', any_parameter_callback)     
# print(" Change THR_MID and THR_MIN parameters (and wait for callback)")    
# vehicle.parameters['THR_MID']=400  
# vehicle.parameters['THR_MIN']=30


# ## Reset variables to sensible values.
# print("\nReset vehicle attributes/parameters and exit")
# vehicle.mode = VehicleMode("STABILIZE")
# #vehicle.armed = False
# vehicle.parameters['THR_MIN']=130
# vehicle.parameters['THR_MID']=500


# #Close vehicle object before exiting script
# print("\nClose vehicle object")
# vehicle.close()

# # Shut down simulator if it was started.
# if sitl is not None:
#     sitl.stop()

# print("Completed")








# # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # Demonstrates how to arm and takeoff in Copter and how to navigate to points using Vehicle.simple_goto.

# # Full documentation is provided at http://python.dronekit.io/examples/simple_goto.html
# # """

# # from __future__ import print_function
# import time
# from dronekit import connect, VehicleMode, LocationGlobalRelative


# # Set up option parsing to get connection string
# import argparse
# parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
# parser.add_argument('--connect',
#                     help="Vehicle connection target string. If not specified, SITL automatically started and used.")
# args = parser.parse_args()

# connection_string = args.connect
# sitl = None


# # Start SITL if no connection string specified
# if not connection_string:
#     import dronekit_sitl
#     sitl = dronekit_sitl.start_default()
#     connection_string = sitl.connection_string()


# # Connect to the Vehicle
# print('Connecting to vehicle on: %s' % connection_string)
# vehicle = connect(connection_string, wait_ready=True)


# def arm_and_takeoff(aTargetAltitude):
#     """
#     Arms vehicle and fly to aTargetAltitude.
#     """

#     print("Basic pre-arm checks")
#     # Don't try to arm until autopilot is ready
#     while not vehicle.is_armable:
#         print(" Waiting for vehicle to initialise...")
#         time.sleep(1)

#     print("Arming motors")
#     # Copter should arm in GUIDED mode
#     vehicle.mode = VehicleMode("GUIDED")
#     vehicle.armed = True

#     # Confirm vehicle armed before attempting to take off
#     while not vehicle.armed:
#         print(" Waiting for arming...")
#         time.sleep(1)

#     print("Taking off!")
#     vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

#     # Wait until the vehicle reaches a safe height before processing the goto
#     #  (otherwise the command after Vehicle.simple_takeoff will execute
#     #   immediately).
#     while True:
#         print(" Altitude: ", vehicle.location.global_relative_frame.alt)
#         # Break and return from function just below target altitude.
#         if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
#             print("Reached target altitude")
#             break
#         time.sleep(1)


# arm_and_takeoff(10)

# print("Set default/target airspeed to 3")
# vehicle.airspeed = 3

# print("Going towards first point for 30 seconds ...")
# point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
# vehicle.simple_goto(point1)

# # sleep so we can see the change in map
# time.sleep(30)

# print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
# point2 = LocationGlobalRelative(-35.363244, 149.168801, 20)
# vehicle.simple_goto(point2, groundspeed=10)

# # sleep so we can see the change in map
# time.sleep(30)

# print("Returning to Launch")
# vehicle.mode = VehicleMode("RTL")

# # Close vehicle object before exiting script
# print("Close vehicle object")
# vehicle.close()

# # Shut down simulator if it was started.
# if sitl:
#     sitl.stop()
    
#     # return to launch,goto,takeoff,vehicle mode need to chage,arm ,yaw



#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2015-2016, 3D Robotics.
vehicle_state.py: 

Demonstrates how to get and set vehicle state and parameter information, 
and how to observe vehicle attribute (state) changes.

Full documentation is provided at http://python.dronekit.io/examples/vehicle_state.html
"""
from __future__ import print_function
from dronekit import connect, VehicleMode
import time

#Set up option parsing to get connection string
# import argparse  
# parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
# parser.add_argument('--connect', 
#                    help="vehicle connection target string. If not specified, SITL automatically started and used.")
# args = parser.parse_args()

# connection_string = args.connect
# sitl = None


# #Start SITL if no connection string specified
# if not connection_string:
#     import dronekit_sitl
#     sitl = dronekit_sitl.start_default()
#     connection_string = sitl.connection_string()


# # Connect to the Vehicle. 
# #   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
s=input()
# print("\nConnecting to vehicle on: %s" % connection_string)
# vehicle = connect(connection_string, wait_ready=True)
vehicle = connect(s, wait_ready=True)

vehicle.wait_ready('autopilot_version')

# Get all vehicle attributes (state)
print("\nGet all vehicle attribute values:")
print(" Autopilot Firmware version: %s" % vehicle.version)
print("   Major version number: %s" % vehicle.version.major)
print("   Minor version number: %s" % vehicle.version.minor)
print("   Patch version number: %s" % vehicle.version.patch)
print("   Release type: %s" % vehicle.version.release_type())
print("   Release version: %s" % vehicle.version.release_version())
print("   Stable release?: %s" % vehicle.version.is_stable())
print(" Autopilot capabilities")
print("   Supports MISSION_FLOAT message type: %s" % vehicle.capabilities.mission_float)
print("   Supports PARAM_FLOAT message type: %s" % vehicle.capabilities.param_float)
print("   Supports MISSION_INT message type: %s" % vehicle.capabilities.mission_int)
print("   Supports COMMAND_INT message type: %s" % vehicle.capabilities.command_int)
print("   Supports PARAM_UNION message type: %s" % vehicle.capabilities.param_union)
print("   Supports ftp for file transfers: %s" % vehicle.capabilities.ftp)
print("   Supports commanding attitude offboard: %s" % vehicle.capabilities.set_attitude_target)
print("   Supports commanding position and velocity targets in local NED frame: %s" % vehicle.capabilities.set_attitude_target_local_ned)
print("   Supports set position + velocity targets in global scaled integers: %s" % vehicle.capabilities.set_altitude_target_global_int)
print("   Supports terrain protocol / data handling: %s" % vehicle.capabilities.terrain)
print("   Supports direct actuator control: %s" % vehicle.capabilities.set_actuator_target)
print("   Supports the flight termination command: %s" % vehicle.capabilities.flight_termination)
print("   Supports mission_float message type: %s" % vehicle.capabilities.mission_float)
print("   Supports onboard compass calibration: %s" % vehicle.capabilities.compass_calibration)
print(" Global Location: %s" % vehicle.location.global_frame)
print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print(" Local Location: %s" % vehicle.location.local_frame)
print(" Attitude: %s" % vehicle.attitude)
print(" Velocity: %s" % vehicle.velocity)
print(" GPS: %s" % vehicle.gps_0)
print(" Gimbal status: %s" % vehicle.gimbal)
print(" Battery: %s" % vehicle.battery)
print(" EKF OK?: %s" % vehicle.ekf_ok)
print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
print(" Rangefinder: %s" % vehicle.rangefinder)
print(" Rangefinder distance: %s" % vehicle.rangefinder.distance)
print(" Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
print(" Heading: %s" % vehicle.heading)
print(" Is Armable?: %s" % vehicle.is_armable)
print(" System status: %s" % vehicle.system_status.state)
print(" Groundspeed: %s" % vehicle.groundspeed)    # settable
print(" Airspeed: %s" % vehicle.airspeed)    # settable
print(" Mode: %s" % vehicle.mode.name)    # settable
print(" Armed: %s" % vehicle.armed)    # settable



# Get Vehicle Home location - will be `None` until first set by autopilot
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    if not vehicle.home_location:
        print(" Waiting for home location ...")
# We have a home location, so print it!        
print("\n Home location: %s" % vehicle.home_location)


# Set vehicle home_location, mode, and armed attributes (the only settable attributes)

print("\nSet new home location")
# Home location must be within 50km of EKF home location (or setting will fail silently)
# In this case, just set value to current location with an easily recognisable altitude (222)
my_location_alt = vehicle.location.global_frame
my_location_alt.alt = 222.0
vehicle.home_location = my_location_alt
print(" New Home Location (from attribute - altitude should be 222): %s" % vehicle.home_location)

#Confirm current value on vehicle by re-downloading commands
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
print(" New Home Location (from vehicle - altitude should be 222): %s" % vehicle.home_location)


print("\nSet Vehicle.mode = GUIDED (currently: %s)" % vehicle.mode.name) 
vehicle.mode = VehicleMode("GUIDED")
while not vehicle.mode.name=='GUIDED':  #Wait until mode has changed
    print(" Waiting for mode change ...")
    time.sleep(1)


# Check that vehicle is armable
while not vehicle.is_armable:
    print(" Waiting for vehicle to initialise...")
    time.sleep(1)
    # If required, you can provide additional information about initialisation
    # using `vehicle.gps_0.fix_type` and `vehicle.mode.name`.
    
#print "\nSet Vehicle.armed=True (currently: %s)" % vehicle.armed 
#vehicle.armed = True
#while not vehicle.armed:
#    print " Waiting for arming..."
#    time.sleep(1)
#print " Vehicle is armed: %s" % vehicle.armed 


# Add and remove and attribute callbacks

#Define callback for `vehicle.attitude` observer
last_attitude_cache = None
def attitude_callback(self, attr_name, value):
    # `attr_name` - the observed attribute (used if callback is used for multiple attributes)
    # `self` - the associated vehicle object (used if a callback is different for multiple vehicles)
    # `value` is the updated attribute value.
    global last_attitude_cache
    # Only publish when value changes
    if value!=last_attitude_cache:
        print(" CALLBACK: Attitude changed to", value)
        last_attitude_cache=value

print("\nAdd `attitude` attribute callback/observer on `vehicle`")     
vehicle.add_attribute_listener('attitude', attitude_callback)

print(" Wait 2s so callback invoked before observer removed")
time.sleep(2)

print(" Remove Vehicle.attitude observer")    
# Remove observer added with `add_attribute_listener()` specifying the attribute and callback function
vehicle.remove_attribute_listener('attitude', attitude_callback)


        
# Add mode attribute callback using decorator (callbacks added this way cannot be removed).
print("\nAdd `mode` attribute callback/observer using decorator") 
@vehicle.on_attribute('mode')   
def decorated_mode_callback(self, attr_name, value):
    # `attr_name` is the observed attribute (used if callback is used for multiple attributes)
    # `attr_name` - the observed attribute (used if callback is used for multiple attributes)
    # `value` is the updated attribute value.
    print(" CALLBACK: Mode changed to", value)

print(" Set mode=STABILIZE (currently: %s) and wait for callback" % vehicle.mode.name) 
vehicle.mode = VehicleMode("STABILIZE")

print(" Wait 2s so callback invoked before moving to next example")
time.sleep(2)

print("\n Attempt to remove observer added with `on_attribute` decorator (should fail)") 
try:
    vehicle.remove_attribute_listener('mode', decorated_mode_callback)
except:
    print(" Exception: Cannot remove observer added using decorator")



 
# Demonstrate getting callback on any attribute change
def wildcard_callback(self, attr_name, value):
    print(" CALLBACK: (%s): %s" % (attr_name,value))

print("\nAdd attribute callback detecting ANY attribute change")     
vehicle.add_attribute_listener('*', wildcard_callback)


print(" Wait 1s so callback invoked before observer removed")
time.sleep(1)

print(" Remove Vehicle attribute observer")    
# Remove observer added with `add_attribute_listener()`
vehicle.remove_attribute_listener('*', wildcard_callback)
    


# Get/Set Vehicle Parameters
print("\nRead and write parameters")
print(" Read vehicle param 'THR_MIN': %s" % vehicle.parameters['THR_MIN'])

print(" Write vehicle param 'THR_MIN' : 10")
vehicle.parameters['THR_MIN']=10
print(" Read new value of param 'THR_MIN': %s" % vehicle.parameters['THR_MIN'])


print("\nPrint all parameters (iterate `vehicle.parameters`):")
for key, value in vehicle.parameters.iteritems():
    print(" Key:%s Value:%s" % (key,value))
    

print("\nCreate parameter observer using decorator")
# Parameter string is case-insensitive
# Value is cached (listeners are only updated on change)
# Observer added using decorator can't be removed.
 
@vehicle.parameters.on_attribute('THR_MIN')  
def decorated_thr_min_callback(self, attr_name, value):
    print(" PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))


print("Write vehicle param 'THR_MIN' : 20 (and wait for callback)")
vehicle.parameters['THR_MIN']=20
for x in range(1,5):
    #Callbacks may not be updated for a few seconds
    if vehicle.parameters['THR_MIN']==20:
        break
    time.sleep(1)


#Callback function for "any" parameter
print("\nCreate (removable) observer for any parameter using wildcard string")
def any_parameter_callback(self, attr_name, value):
    print(" ANY PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))

#Add observer for the vehicle's any/all parameters parameter (defined using wildcard string ``'*'``)
vehicle.parameters.add_attribute_listener('*', any_parameter_callback)     
print(" Change THR_MID and THR_MIN parameters (and wait for callback)")    
vehicle.parameters['THR_MID']=400  
vehicle.parameters['THR_MIN']=30


## Reset variables to sensible values.
print("\nReset vehicle attributes/parameters and exit")
vehicle.mode = VehicleMode("STABILIZE")
#vehicle.armed = False
vehicle.parameters['THR_MIN']=130
vehicle.parameters['THR_MID']=500


#Close vehicle object before exiting script
print("\nClose vehicle object")
vehicle.close()

# Shut down simulator if it was started.
if sitl is not None:
    sitl.stop()

print("Completed")