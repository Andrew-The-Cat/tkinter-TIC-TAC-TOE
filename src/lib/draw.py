from math import sqrt
from tkinter import Canvas

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def draw(self):
        pass

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # position vector adition for points
    def __add__(self, other):
        return Point( self.x + other.x, self.y + other.y )
    
    # position vector subtraction for points
    def __sub__(self, other):
        return Point( self.x - other.x, self.y - other.y )
    
    def draw(self, canvas:Canvas, colour, radius:int = 5):
        canvas.create_oval(self.x - radius, self.y - radius, self.x + radius, self.y + radius, fill=colour)

class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y

        self.length = sqrt ((self.__x1 - self.__x2) ** 2 + (self.__y1 - self.__y2) ** 2)

    def draw(self, canvas:Canvas, colour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=colour, width = 2)

class Triangle:
    def __init__(self, p1:Point, p2:Point, p3:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
        x1 = p1.x
        x2 = p2.x
        x3 = p3.x

        y1 = p1.y
        y2 = p2.y
        y3 = p3.y

        self.det = x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1*y3

        self.area = abs(self.det) / 2

    def draw(self, canvas:Canvas, colour):
        canvas.create_polygon(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)