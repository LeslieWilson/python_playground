#open a graphics window
win = GraphWin('Shapes')
#draw a red circle centered at point (100, 100) with radius 30
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
#put a textual label in teh center of the circle
label = Text(center, "Red Circle")
label.draw(win)
#draw a square using a rectangle object
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)
#draw a line segment using a line objects
line = Line(Point(20,30), Point(180,165))
line.draw(win)
# draw an oval using the Oval object
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)

# examples

# leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = leftEye.clone()
# above makes right the same as left
righEye.move(20, 0)
head = Circle(Point 90,50),50)

rightEye.draw(win)
leftEye.draw(win)
head.draw(win)

# GRAPH example

def main ():
    #Introduction
    print "This program plots the growth of a 10-year investment"

    #get principle and interest rate
    principal = input ("enter the initial principal: ")
    apr = input ("enter the annualized interest rate: ")

    #create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20,230), ' 0.0K').draw(win)
    Text(Point(20,180), ' 2.5K').draw(win)
    Text(Point20,130), ' 5.0K').draw(win)

    # draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65,230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # draw bars for sucessive years
    for year in range(1,11):
        #calculate value for the next year
        principal = principal * (1 + apr)
        #draw bar for this value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230), Point(x11+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    raw_input("Press <Enter> to quit")
