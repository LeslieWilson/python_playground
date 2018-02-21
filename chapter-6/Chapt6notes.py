# CHAPTER SIX NOTES!

# functions are a small program inside of a program. write a sequence of statements and give that sequence name

def happy():
    print "Happy birthday to you!"

    # defined function called happy

def singFred():
    happy()
    happy()

def singLucy():
    happy()
    happy()

def main():
    singFred()
    sing Lucy()

# make generic function called sing:

def sing(person):
    happy()
    happy()
    print "happy birthday, dear" , person + "."
    happy()

# function that sings, then, for three people

def main():
    sing("fred")
    print
    sing("leslie")
    print
    sing("bob")


    # make a function that tells two dogs they are a good boy, twice

    def compliment():
        print "theres a good boy"

    def petting(dog):
        compliment()
        compliment(), + dog

    def main():
        dog("leslie")
        print
        dog("sam")
        print


        # scope refers to the places in a prgram where a given variable may be referenced. the variables used in a function are local to that function. the only way to share variables is for them to be passed in as a parameter.

        # program: Triangle2.py
        import math
        from graphics import *

        def square(x)
        return x * x

        def distance(p1,p2):
            dist = math.sqrt(square(p2.getX() - p1.getX())
                            + square(p2.getY() - p1.getY()))
            return dist

        def main():
            win = GrapgWin("draw a triangle")
            win.setCoords(0.0, 0.0, 10.0, 10.0)
            message = Text(Point(5, 0.5), "click on three points")
            message.draw(win)

            #get and draw three verticies of Triangle
            p1 = win.getMouse()
            p1.draw(win)
            p2 = win.getMouse()
            p2.draw(win)
            p3 = win.getMouse()
            p3.draw(win)

            # use polygon object to draw the Triangle
            triangle = Polygon(p1,p2,p3)
            triangle.setFill("peachpuff")
            triangle.setOutline("cyan")
            triangle.draw(win)

            # calculate the perimeter of the triangle
            perim = distance(p1,p2) + distance(p2,p3) + distance (p3,p1)
            message.setText("the perimeter is: %0.2f" % perim)

            # wait for anothe rlcick to exist
            win.getMouse()
            win.close()

            
