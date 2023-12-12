from __future__ import print_function
from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
from dronekit_sitl import SITL

      # user = request.form['nm']
# Create SITL instance
# sitl = SITL()
# sitl.download('copter', '3.6', verbose=True) 
# sitl_args = ['--home=lat,lon']
# sitl.launch(sitl_args)
s=input()
# print("\nConnecting to vehicle on: %s" % connection_string)
# vehicle = connect(connection_string, wait_ready=True)
vehicle = connect(s, wait_ready=True,timeout=60)
long=78.489019
lat=17.396509
point1 = LocationGlobalRelative(lat,long,20)
# vehicle.home_location(point1)
try:
    vehicle = connect(s, wait_ready=True, timeout=60)
    print("Vehicle connected!")
except Exception as e:
    print(f"Failed to connect: {str(e)}")
alt=int(input())
# vehicle.wait_ready('autopilot_version')
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
vehicle.simple_takeoff(alt)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
while True:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    # Break and return from function just below target altitude.
    if vehicle.location.global_relative_frame.alt >= alt:
        print("Reached target altitude")
        break
    time.sleep(1)
# long=78.4875251
# lat=17.3988
point1.yaw=350
print("goto!")
vehicle.simple_goto(point1) 
while True:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    # Break and return from function just below target altitude.
    print("Reached location",vehicle.location.global_relative_frame,lat*10000,long*10000)
    if int(vehicle.location.global_relative_frame.lat*10000) ==int(lat*10000) and int(vehicle.location.global_relative_frame.lon*10000) ==int(10000*long):
        print("Reached location",vehicle.location.global_relative_frame)
        break
    time.sleep(1)
vehicle.mode = VehicleMode("RTL")
vehicle.RTL_ALT=2000
# : The minimum altitude the copter will move to before returning to launch.

# Set to zero to return at the current altitude.

# The return altitude can be set from 1 to 8000 centimeters.

# The default return altitude Default is 15 meters (1500)

vehicle.RTL_ALT_FINAL=0
# : The altitude the copter will move to at the final stage of “Returning to Launch” or after completing a Mission.

# Set to zero to automatically land the copter.

# The final return altitude may be adjusted from 0 to 1000 centimeters.

vehicle.RTL_LOIT_TIME=5000
# : Time in milliseconds to hover/pause above the “Home” position before beginning final descent.

# The “Loiter” time may be adjusted from 0 to 60,000 milliseconds.

WP_YAW_BEHAVIOR=0
# : Sets how the autopilot controls the “Yaw” during Missions and RTL.

# 0 = Never change Yaw.

# 1 = Face Next Waypoint including facing home during RTL.

# 2 = Face Next Waypoint except for RTL (i.e. during RTL vehicle will remain pointed at its last heading)

LAND_SPEED=25
# : The descent speed for the final stage of landing in centimeters per second.

# The landing speed is adjustable from 20 to 200 centimeters per second.

# RTL_CLIMB_MIN: The vehicle will climb at least this many meters at the first stage of the RTL. By default this value is zero. (only Copter-3.3 and above)

# RTL_SPEED: The horizontal speed (in cm/s) at which the vehicle will return to home. By default this value is zero meaning it will use WPNAV_SPEED. (only Copter-3.4 and higher)

# RTL_CONE_SLOPE: Defines the slope of an inverted cone above home which is used to limit the amount the vehicle climbs when RTL-ing from close to home. Low values lead to a wide cone meaning the vehicle will climb less, High values will lead to the vehicle climbing more. (supported in Copter-3.4 and higher)
