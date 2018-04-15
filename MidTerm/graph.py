"""
Leslie Wilson
Sunday April 15, 2018
graph.py

"""

# THIS FILE IS THE LAST THAT NEEDS TO BE RUN. IT TAKES THE COUNTS OF ALL THOSE DIFFERENT ACADEMIC CATEGORIES BY DEFINING COUNT AS THE INTEGER THAT COMES IN THE SECOND INDEX OF EACH CSV FILE LINE. IT READS THOUGH THE COUNTS AND MAKES A GRAPH, CREATEGRAPH IS READING THE COUNTS FROM DATA.TXT


from graphics import *

"""imports the graphics library from python"""

def createGraph(fileName):
    """function takes a text file and draws a graph"""

    counts = open(fileName, "r")
    lineNumber = counts.readline()
    graph = GraphWin("Counts", 400, 400)
    graph.setCoords(-15, 0, 15, int(lineNumber) * 3)

#Loop though the score in the file to draw a graph
    yAxisCount = 1
    for line in counts:
        splitLine = line.split()
        count = int(splitLine[1])
        name = splitLine[0]

#initiate graph bars
        bar = Rectangle((Point(0,yAxisCount)), (Point(count, yAxisCount + 2)))
        bar.draw(graph)
        bar.setFill('pink')

#initiate text
        text = Text(Point(-7, yAxisCount
        + 1), name)
        text.draw(graph)
        yAxisCount +=3
    graph.getMouse()

createGraph("Data.txt")
