#!/usr/bin/env python3

import math as m

"""
essential engine physics
"""

frameRate = 60

timeEnd = 10  # length of simulation in seconds

# simulation params
throttleTime = 2  # in seconds
energyMaxThrottle = 1000   # in Joules, max throttle is 1.0

# simulation state
time = 0  # current time in seconds


# vehicle params
engineCrankMass     = 20  # in kilograms
engineCrankRadius   = 5/100 # in meters, e.g. 5/100 = 5 cm
engineCrankMomentum = 0.5 * engineCrankMass * m.pow( engineCrankRadius, 2 )
engineCrankFriction = 3  # Joules/RPM

# vehicle state
engineCrankRPM = 0
throttle = 0
velocity = 0
while time < timeEnd:

    # compute throttle
    if time < throttleTime:
        throttle = time / throttleTime
    else:
        throttle = 0

    # compute energy in
    energyIn = throttle / energyMaxThrottle

    # current kinetic energy of engine
    engineKinetic = 0.5 * engineCrankMomentum * ( enginerCrankRPM / 60 * 2 * 3.14159 )
    
    

    print( f'{time}, {throttle}, {engineCrankRPM}, {engineKinetic}, {velocity}' )

    time += 1 / frameRate
    

