from graphics import *

# opens fileName
def main(fileName):
    scores = open(fileName, "r")
    lineNumber = scores.readline()
    graph = GraphWin("test scores", 500, 500)
    # 15 units of space for the names, 100 units on the x axis,
    graph.setCoords(-15, 0, 100, int(lineNumber) * 4)

# going up and down the y axis
    vertaxis = 1
    for line in scores:
        separate = line.split()
        score2 = int(separate[1])
        name = separate[0]
        bar = Rectangle((Point(0, vertaxis)), (Point(score2, vertaxis + 2)))

        # makes label
        text = Text(Point(-7, vertaxis + 1), name)
        text.draw(graph)

        # makes bar
        bar.setFill("red")
        bar.draw(graph)
        vertaxis += 3



    graph.getMouse()

main("txt2.txt")
