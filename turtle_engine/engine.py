import math
import turtle
from tkinter import *

class Circle:
    def __init__(self, x, y, radius, line_color, line_thickness, bg_color):
        self.center = (x, y)
        self.line_color = line_color
        self.line_thickness = line_thickness
        self.bg_color = bg_color
        self.radius = radius

    def draw(self):
        pen = turtle
        pen.pencolor(self.line_color)
        pen.fillcolor(self.bg_color)
        pen.pensize(self.line_thickness)
        pen.pu()
        pen.goto(self.center[0], self.center[1])
        pen.seth(270)
        pen.fd(self.radius)
        pen.seth(0)
        pen.pd()
        pen.begin_fill()
        pen.circle(self.radius)
        pen.end_fill()

class RegularPolygon:
    def __init__(self, x, y, n_sides, side_size, line_color, line_thickness, bg_color):
        self.center = (x, y)
        self.n_sides = n_sides
        self.side_size = side_size
        self.line_color = line_color
        self.line_thickness = line_thickness
        self.bg_color = bg_color
        self.inner_angle = (180.0 * self.n_sides - 360) / self.n_sides
        self.radius = self.side_size / (2.0 * math.sin(math.radians(180.0 / self.n_sides)))
        self.apothem = self.side_size / (2.0 * math.tan(math.radians(180.0 / self.n_sides)))

    def draw(self):
        pen = turtle
        pen.pencolor(self.line_color)
        pen.fillcolor(self.bg_color)
        pen.pensize(self.line_thickness)
        pen.pu()
        pen.goto(self.center[0], self.center[1])
        pen.seth(-90)
        pen.fd(self.apothem)
        pen.seth(0)
        pen.fd(self.side_size / 2.0)
        pen.pd()
        pen.begin_fill()
        for s in range(self.n_sides):
            pen.lt(180 - self.inner_angle)
            pen.fd(self.side_size)
        pen.end_fill()

class Rectangle:
    def __init__(self, x, y, side1, side2, line_color, line_thickness, bg_color):
        self.center = (x, y)
        self.side1, self.side2 = side1, side2
        self.line_color = line_color
        self.line_thickness = line_thickness
        self.bg_color = bg_color

    def draw(self):
        pen = turtle
        pen.pencolor(self.line_color)
        pen.fillcolor(self.bg_color)
        pen.pensize(self.line_thickness)
        pen.pu()
        pen.goto(self.center[0], self.center[1])
        pen.seth(270)
        pen.fd(self.side1 / 2.0)
        pen.seth(0)
        pen.fd(self.side2 / 2.0)
        pen.seth(90)
        pen.pd()
        pen.begin_fill()
        pen.fd(self.side1)
        pen.seth(180)
        pen.fd(self.side2)
        pen.seth(270)
        pen.fd(self.side1)
        pen.seth(0)
        pen.fd(self.side2)
        pen.end_fill()

class Trapezium:
    def __init__(self, x, y, top_base, bottom_base, height, line_color, line_thickness, bg_color):
        self.center = (x, y)
        self.top_base = top_base
        self.bottom_base = bottom_base
        self.height = float(height)
        self.line_thickness = line_thickness
        self.line_color = line_color
        self.bg_color = bg_color
        self.side = math.sqrt(self.height ** 2 + ((max([self.bottom_base, self.top_base]) - min([self.bottom_base, self.top_base])) / 2.0) ** 2)
        if self.bottom_base > self.top_base:
            self.bottom_angle = math.degrees(math.asin(self.height / self.side))
            self.top_angle = 180 - self.bottom_angle
        else:
            self.top_angle = math.degrees(math.asin(self.height / self.side))
            self.bottom_angle = 180 - self.top_angle

    def draw(self):
        pen = turtle
        pen.pencolor(self.line_color)
        pen.fillcolor(self.bg_color)
        pen.pensize(self.line_thickness)
        pen.pu()
        pen.goto(self.center[0], self.center[1])
        pen.seth(270)
        pen.fd(self.height / 2.0)
        pen.seth(0)
        pen.fd(self.bottom_base / 2.0)
        pen.lt(180 - self.bottom_angle)
        pen.pd()
        pen.begin_fill()
        pen.fd(self.side)
        pen.seth(180)
        pen.fd(self.top_base)
        pen.lt(180 - self.top_angle)
        pen.fd(self.side)
        pen.seth(0)
        pen.fd(self.bottom_base)
        pen.end_fill()

class Lozenge:
    def __init__(self, x, y, height, width, line_color, line_thickness, bg_color):
        self.center = (x, y)
        self.height = height
        self.width = width
        self.line_color = line_color
        self. line_thickness = line_thickness
        self.bg_color = bg_color

        self.side = math.sqrt((self.height / 2)**2 + (self.width / 2)**2)
        self.w_angle = math.degrees(math.asin((self.height / 2.0)/self.side)) * 2
        self.h_angle = math.degrees(math.asin((self.width / 2.0)/self.side)) * 2

    def draw(self):
        pen = turtle
        pen.pencolor(self.line_color)
        pen.fillcolor(self.bg_color)
        pen.pensize(self.line_thickness)
        pen.pu()
        pen.goto(self.center[0], self.center[1])
        pen.seth(270)
        pen.fd(self.height / 2.0)
        pen.lt(180 - self.h_angle / 2.0)
        pen.begin_fill()
        pen.pd()
        pen.fd(self.side)
        pen.lt(180 - self.w_angle)
        pen.fd(self.side)
        pen.lt(180 - self.h_angle)
        pen.fd(self.side)
        pen.lt(180 - self.w_angle)
        pen.fd(self.side)
        pen.end_fill()

class Text:
    def __init__(self, x, y, text, font_size=15, font="Arial", font_color="black", font_type='normal', align='left'):
        self.center = (x, y)
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.font_type = font_type
        self.align = align

    def draw(self):
        pen = turtle
        pen.pencolor(self.font_color)
        pen.pu()
        pen.goto(self.center[0], self.center[1])
        pen.pd()
        pen.write(self.text, move=False, align=self.align, font=(self.font, self.font_size, self.font_type)) 
        
class Line:
    def __init__(self, x1, y1, x2, y2, line_color="black", line_thickness=5):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.line_color = line_color
        self.line_thickness = line_thickness
        
    def draw(self):
        pen = turtle
        pen.pencolor(self.line_color)
        pen.pensize(self.line_thickness)
        pen.pu()
        pen.goto(self.x1, self.y1)
        pen.pd()
        pen.goto(self.x2, self.y2)
        
class Dot:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        
    def draw(self):
        pen = turtle
        pen.pencolor(self.color)
        pen.pu()
        pen.goto(self.x, self.y)
        pen.pd()
        turtle.dot(self.size, self.color)
        
class Window:
    def __init__(self, title="Engine"):
        self.title = title
        self.screen = turtle.Screen()
        self.screen.setup(width=1.0, height=0.75, startx=-1, starty=1)
        self.screen.colormode(255)
        self.screen.bgcolor("#ffffff")
        self.screen.title(title)
        self.pen = turtle.Pen()
        self.pen.ht()
        self.pen.speed("fastest")
        self.pen.shape("circle")
        
    def clear_screen(self):
        turtle.reset()
        
window = Window()
square = Rectangle(0, 0, 50, 50, 'blue', 5, 'light blue')
square.draw()
    

