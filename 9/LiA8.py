import turtle

'''
Create by Dongning Li (Donnie)
SWE 5001 Software Engineering 1
Assignment 8
11/05/2016
'''


class Canvas:
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.visibleObjects = []
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=self.width,height=self.height)
        self.turtle.hideturtle()

    def drawAll(self):
        self.screen.reset()
        self.turtle.up()
        self.screen.tracer(0)
        for shape in self.visibleObjects:
            shape._draw(self.turtle)
        self.screen.tracer(1)
        self.turtle.hideturtle()

    def addShape(self,shape):
        self.visibleObjects.append(shape)

    def draw(self,gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.turtle.up()
        self.screen.tracer(0)
        gObject._draw(self.turtle)
        self.screen.tracer(1)
        self.addShape(gObject)
        
    def freeze(self):
            self.screen.exitonclick()
            

class GeometricObject:
    def __init__(self):
        self.lineColor = 'black'
        self.lineWidth = 3
        self.visible = False
        self.myCanvas = None

    def setColor(self,color):
        self.lineColor = color
        if self.visible:
            self.myCanvas.drawAll()

    def setWidth(self,width):
        self.lineWidth = width
        if self.visible:
            self.myCanvas.drawAll()

    def getColor(self):
        return self.lineColor

    def getWidth(self):
        return self.lineWidth

    def _draw(self):
        print ("Error: You must define _draw in subclass")

    def setVisible(self,vFlag):
        self.visible = vFlag

    def setCanvas(self,theCanvas):
        self.myCanvas = theCanvas
        
        
class Line(GeometricObject):
    def __init__(self, p1,p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
    
    def getP1(self):
        return self.p1
        
    def getP2(self):
        return self.p2
        
    def _draw(self,aturtle):
        aturtle.color(self.getColor())
        aturtle.width(self.getWidth())
        aturtle.goto(self.p1.getCoord())
        aturtle.down()
        aturtle.goto(self.p2.getCoord())
        
            
class Point(GeometricObject):
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y

    def getCoord(self):
        return (self.x,self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def _draw(self,aturtle):
        aturtle.goto(self.x,self.y)
        aturtle.dot(self.lineWidth,self.lineColor) 
        
        
class Shape(GeometricObject):
    def __init__(self):
        super().__init__()
        self.fillColor = None
        
    def setFill(self,color):
        self.fillColor = color
        if self.visible:
            self.myCanvas.drawAll()
        
        
class Polygon(Shape):
    def __init__(self, corners):
        super().__init__()
        self.corners = corners
        
    def _draw(self,aturtle):
        aturtle.color(self.getColor())
        aturtle.width(self.getWidth())
        
        if self.fillColor:
            aturtle.begin_fill()
            aturtle.fillcolor(self.fillColor)
            
        aturtle.goto(self.corners[0].getCoord())
        aturtle.down()
            
        for iCorner in range(1, len(self.corners)):
            aturtle.goto(self.corners[iCorner].getCoord())
            
        aturtle.goto(self.corners[0].getCoord())
        aturtle.up()
        
        if self.fillColor:
            aturtle.end_fill()
    
    def move(self, deltaX, deltaY):
            
        for iCorner in range(len(self.corners)):
            corner = self.corners[iCorner]
            self.corners[iCorner] = Point(corner.getX() + deltaX, corner.getY() + deltaY)

        if self.visible:
            self.myCanvas.drawAll()
       
    
class Rectangle(Polygon):
    def __init__(self, lowerLeft, upperRight):
        super().__init__([
            Point(lowerLeft.getX(), lowerLeft.getY()),
            Point(upperRight.getX(), lowerLeft.getY()),
            Point(upperRight.getX(), upperRight.getY()),
            Point(lowerLeft.getX(), upperRight.getY())
        ])
        self.lowerLeft = lowerLeft
        self.upperRight = upperRight
        
    def getLowerLeft(self):
        return self.lowerLeft
        
    def getUpperRight(self):
        return self.upperRight
   
        
class Triangle(Polygon):
    def __init__(self, p1, p2, p3):
        super().__init__([p1, p2, p3])
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def getP1(self):
        return self.p1
        
    def getP2(self):
        return self.p2
        
    def getP3(self):
        return self.p3
        
        
class Square(Rectangle):
    def __init__(self, lowerLeft, upperRight):
        super().__init__(lowerLeft, upperRight)
