# NOTES:

"""
This is a program that takes the card written in the previous program, and puts it into a card-shooter-gun. You aim the card-shooter-gun at a cop, and it shoots a random playing card in his face at a certain velocity. I want to figure out how far the playing card will travel when fired at gun angles and initial velocities. The input to the program will be the launch angle in degrees. the inititial velocity (in meters per second) and the initial height(in meters) of the gun itself. woill need to upate the position of the card to account for its flight.

fires a random card, the name of the card displays, if you input it at 200 mph the cop will be injured, at less it won't hurt


gun is the class... initilaize a gun, the gun is going to take a card and a speed, and its going to have a method called fire which will eject the card and maybe injure the cop. will print if cop gets hurt.

1.have method called reload, which puts new card into gun.

2. method checks currently loaded

3. method that fires a blank and returns a string

4. method that fires it at a random speed.

"""

from random import *
from elevenProblem import *

class Gun(object):
    def __init__(self):
        self.ammunition = randomCard()
        self.loaded = self.ammunition[0]

# what ammo do i have?
    def getAmmo(self):
        print "you're loaded with:",
        for i in self.ammunition:
            print i,
        print "\n"

# what speed is it being shot at

    def getSpeed(self):
        vel = input("enter the initial velocity(in MPH): ")
        if vel <= 5:
            print " womp womp "
        elif vel > 5:
            print "OW"


    def reLoad(self):

        return self.reload

    def fire(self):
        shot = self.loaded
        self.loaded = nil
        print "cop got hit by %s" % (shot)


# this makes makes ammo and puts it in

def main():
    gun = Gun()
    gun.getAmmo()
    gun.getSpeed()

main()









# def kard():
#     ammunition = randomCard()
#     return ammunition
#
# #convert angle to radians
# theta = math.pi * angle/180.0
#
# #set initial position and velocities in x and y directions
# xpos = 0
# ypos = h0
# xvel = vel * cos(theta)
# yvel = vel * sin(theta)
#
# # loop until card hits his face
# while ypos >= 0:
#     # calculate position and velocity in time seconds
#     xpos = xpos + time * xvel
#     yvell = yvel - time + 9.8
#     ypos = ypos + time * (yvel + yvell) /2.0
#     yvel = yvel;
#
#
#     print "\nDistance traveled: %0 if meters" % (xpos)
# while ypos
