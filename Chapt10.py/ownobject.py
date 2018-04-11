NOTES:

"""
This is a program that takes the card written in the previous program, and puts it into a card-shooter-gun. You aim the card-shooter-gun at a cop, and it shoots a random playing card in his face at a certain velocity. I want to figure out how far the playing card will travel when fired at gun angles and initial velocities. The input to the program will be the launch angle in degrees. the inititial velocity (in meters per second) and the initial height(in meters) of the gun itself. woill need to upate the position of the card to account for its flight.



"""

from random import *
from math import *
from IMPORT CARD

def main():
    angle = input("enter the launch angle(in degrees): ")
    vel = input("enter the initial velocity(in meters/sec): ")
    h0 = input("enter the initial height(in meters): ")
    time = input("enter the time interval between position calculations: ")



#convert angle to radians
theta = math.pi * angle/180.0

#set initial position and velocities in x and y directions
xpos = 0
ypos = h0
xvel = vel * cos(theta)
yvel = vel * sin(theta)

# loop until card hits his face
while ypos >= 0:
    # calculate position and velocity in time seconds
    xpos = xpos + time * xvel
    yvell = yvel - time + 9.8
    ypos = ypos + time * (yvel + yvell) /2.0
    yvel = yvel;;


    print "\nDistance traveled: %0 if meters" % (xpos)
while ypos >
