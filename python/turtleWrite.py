import turtle
import math
import time

import turtle
wn = turtle.Screen()

##wn.tracer(2) 

turt = turtle.Turtle()

turt.begin_fill()
turt.speed(0)
turt.pensize(5)

LETTER_DISTANCE = 10
LETTER_SIZEX = 20
LETTER_SIZEY = 50

turt.penup()
##turt.goto(-turtle.window_width()/2 + LETTER_SIZEX, turtle.window_height()/2 - LETTER_SIZEY - 20)

class letter:
    def __init__(self, point, size =1, spacing = 0):
        self.point = point
        self.size = size
        self.spacing = spacing

class Point:
    def __init__(self, x, y, pen = True):
        self.x = x
        self.y = y
        self.pen = pen
        
    def __str__(self):
        return f"x:{self.x} y:{self.y} pen:{self.pen}"

spawnPoint = Point(turt.xcor(), turt.ycor())

letters = {
    'a' : letter([Point(0.5 , 1) , Point(0.25, 0.5 , False), Point(0.75, 0.5), Point(0.5, 1, False), Point(1, 0)]),
    'b' : letter([Point(0 , 1) , Point(0.5, 1), Point(1, 0.5), Point(0, 0.5), Point(0,0), Point(1, 0), Point(1, 0.5)]),
    'c' : letter([Point(0 , 1) , Point(1, 1), Point(0, 0, False), Point(1, 0)]),
    'd' : letter([Point(0 , 1) , Point(0.5, 1), Point(1, 0.5), Point(1, 0), Point(0,0)]),
    'e' : letter([Point(0 , 1) , Point(1, 1), Point(0, 0.5, False), Point(1, 0.5), Point(0,0, False), Point(1,0)]),
    'f' : letter([Point(0 , 1) , Point(1, 1), Point(0, 0.5, False), Point(1, 0.5)]),
    'g' : letter([Point(0 , 1) , Point(1, 1), Point(0, 0, False), Point(1, 0), Point(1, 0.5), Point(0.5, 0.5)]),
    'h' : letter([Point(0 , 1) , Point(1, 0, False), Point(1, 1), Point(0, 0.5, False), Point(1, 0.5)]),
    'i' : letter([Point(0, 1)], 0.2, 0.2),
    'j' : letter([Point(0 , 0.5) , Point(0, 0), Point(1, 0), Point(1, 1)]),
    'k' : letter([Point(0 , 1) , Point(0, 0.5), Point(1, 1), Point(0, 0.5, False), Point(1, 0)]),
    'l' : letter([Point(0 , 1) , Point(0, 0), Point(1, 0)]),
    'm' : letter([Point(0 , 1) , Point(0.5, 0.5), Point(1, 1), Point(1, 0)]),
    'n' : letter([Point(0 , 1) , Point(1, 0), Point(1, 1)]),
    'o' : letter([Point(0 , 1) , Point(1, 1), Point(1, 0), Point(0, 0)]),
    'p' : letter([Point(0 , 1) , Point(1, 1), Point(1, 0.5), Point(0, 0.5)]),
    'q' : letter([Point(0 , 1) , Point(1, 1), Point(1, 0), Point(0, 0), Point(1,0), Point(0.5, 0.5)]),
    'r' : letter([Point(0 , 1) , Point(1, 1), Point(1, 0.5), Point(0, 0.5), Point(0.5,0.5), Point(1,0)]),
    's' : letter([Point(1 , 0) , Point(1, 0.5), Point(0, 0.5), Point(0, 1), Point(1, 1)]),
    't' : letter([Point(0.5 , 0, False) , Point(0.5, 1), Point(0,1), Point(1,1)]),
    'u' : letter([Point(0 , 1) , Point(0, 0), Point(1, 0), Point(1,1)]),
    'v' : letter([Point(0 , 1, False) , Point(0.5, 0), Point(1,1)]),
    'w' : letter([Point(0 , 1) , Point(0,0), Point(0.5, 0.5), Point(1, 0), Point(1, 1)]),
    'x' : letter([Point(1 , 1) , Point(0, 1, False), Point(1,0)]),
    'y' : letter([Point(1 , 1) , Point(0, 1, False), Point(0.5,0.5)]),
    'z' : letter([Point(0 , 1, False) , Point(1, 1), Point(0,0), Point(1,0)]),
    '.' : letter([Point(0 , 0)], 0.1),
    ',' : letter([Point(0, 0.125, False), Point(-0.25,-0.125)], 0.1),
    ';' : letter([Point(0 , 0.5, False), Point(0, 0.5), Point(0, 0.125, False) , Point(-0.25,-0.125)], 0.1),
    '-' : letter([Point(0 , 0.5, False), Point(0.5, 0.5)], 0.5),
    "'" : letter([Point(0 , 1, False), Point(0, 0.65)], 0.1),
    " " : letter([Point(0,0,False)]),
    '\n': "\n"
}

def angledPoint(point, angle):
    rad = math.radians(angle)
    _x = point.x + math.sin(rad)
    _y = point.y + math.cos(rad)
    return Point(_x, _y, point.pen)


def draw(char, sizex = LETTER_SIZEX , sizey = LETTER_SIZEY):
    let = letters[char]
    
    if let == "\n":
        turt.goto(spawnPoint.x, turt.ycor() - LETTER_SIZEY - 20)
        return
    
    initial = Point(turt.xcor(), turt.ycor())
    
    if(let.spacing != 0):
        turt.penup
        turt.goto(initial.x + (let.spacing * sizex), initial.y)
    
    points = let.point
    for point in points:
        turt.pendown() if point.pen else turt.penup()
        turt.goto(initial.x + (let.spacing * sizex) + point.x * sizex, initial.y + point.y * sizey)
        
    turt.penup()
    turt.goto(initial.x + ((let.spacing + let.size) * sizex) + LETTER_DISTANCE, initial.y)
        
        
def write(text):
    for char in text:
        draw(char.lower()) 

turt.pendown()

turt.goto(0,0)

pos = angledPoint(Point(1,0), 45)
turt.goto(pos.x * 50, pos.y * 50)

pos = angledPoint(Point(1,1), 45)
turt.goto(pos.x * 50, pos.y * 50)

pos = angledPoint(Point(0,1), 45)
turt.goto(pos.x * 50, pos.y * 50)

turt.goto(0,0)


def draw(char, sizex = LETTER_SIZEX , sizey = LETTER_SIZEY):
    let = letters[char]

    points = let.point
    
    turt.goto(angledPoint(Point(0,0), 20))
    
    for point in points:
        
        turt.goto(initial.x + (let.spacing * sizex) + point.x * sizex, initial.y + point.y * sizey)
        
    turt.penup()
    turt.goto(initial.x + ((let.spacing + let.size) * sizex) + LETTER_DISTANCE, initial.y)


##write("""A""")
    
    
##wn.update() 
wn.mainloop() 

