# NOTES:

"""
Leslie Wilson
April 12 2018
ownObject.py

"""

from random import *
from elevenProblem import randomCard

class Gun(object):

    ''' creates gun object with ammunition that is random cards'''

    def __init__(self):
        self.ammunition = randomCard()
        self.loaded = self.ammunition[0]


    def getAmmo(self):

        '''prints the random card array that is your ammunition'''

        print "you're loaded with:",
        for i in self.ammunition:
            print i,


# what speed is it being shot at

    def getSpeed(self):

        '''prompts user for desired speed of ammunition before it fires. determines if person lives or dies- under 40mph will not kill them'''

        vel = input("set your ammos velocity(in MPH): ")
        if vel <= 40:
            print " this is not gonna do much "
        elif vel > 40:
            print "GOOD this will kill him for sure....."
            return vel

    def fire(self):

        '''shoots the first card out of the array at the given speed, if fast enough, kills person. prints the card that killed them'''

        shot = raw_input("pull trigger? y/n: ")
        if shot == "y" and self.getSpeed() > 40:
            print "...yep, you killed him with %s" % (self.loaded)
            self.ammunition.pop(0)
            # print "cop got hit by %s" % (shot)
        elif shot == "n":
            print "you chose not to fire"
        else:
            print "oops you missed the trigger"


    def reLoad(self):

        '''prompts user to reload desired number of cards into shooter. new cards append onto cards still remaining in shooter. prints new list'''

        load = raw_input("you shot the first card in the queue. reload? y/n: ")
        if load == "y":
            self.ammunition += randomCard()
            print "now you're loaded with: ",
            for i in self.ammunition:
                print i,



# this makes makes ammo and puts it in

def main():
    gun = Gun()
    gun.getAmmo()
    gun.fire()
    gun.reLoad()
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
