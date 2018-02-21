# leftEye = Circle(Point(80, 50), 5)
# leftEye.setFill('yellow')
# leftEye.setOutline('red')
# rightEye = leftEye.clone()
# # above makes right the same as left
# righEye.move(20, 0)
# head = Circle(Point 90,50),50)
#
# rightEye.draw(win)
# leftEye.draw(win)
# head.draw(win)
from graphics import *

'''
This program draws a face using python GUI 
'''
def main():

    win = GraphWin("Face Window", 550, 550)

    #left and right eye
    lefteye = righteye.clone()
    lefteye.move(250, 150)
    lefteye.draw(win)
    righteye = Circle(Point(300, 300), 170)
    righteye.setFill("yellow")
    righteye.draw(win)

    # Nose

    #Head
    face = Circle(Point(350, 350), 300)
    face.draw(win)

    #Mounth
    mouth = Oval(Point(270, 380), Point(420, 430))
    mouth.draw(win)

    #win remains
    text = Text(Point(230,500), "Window Close")
    text.draw(win)
    win.getMouse()

main()
