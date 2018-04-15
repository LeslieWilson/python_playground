from graphics import *

#function takes a text file of test scores and draws a graph
def createGraph(fileName):
    testScores = open(fileName, "r")
    lineNumber = testScores.readline()
    graph = GraphWin("test scores", 400, 400)
    graph.setCoords(-15, 0, 15, int(lineNumber) * 3)

#loop though the score in the file to draw a graph


    yAxisCount = 1
    for line in testScores:
        splitLine = line.split()
        testScore = int(splitLine[1])
        name = splitLine[0]

        #initiate graph bars
        bar = Rectangle((Point(0,yAxisCount)), (Point(testScore, yAxisCount + 2)))
        bar.draw(graph)
        bar.setFill('pink')


        #initiate text

        text = Text(Point(-7, yAxisCount
        + 1), name)
        text.draw(graph)
        yAxisCount +=3
    graph.getMouse()

createGraph("Data.txt")
