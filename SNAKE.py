# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 20:31:25 2018

@author: lac35158
"""

import turtle
from random import randint

SIZE = 850

SCREEN = turtle.Screen()
SCREEN.title("snake")
SCREEN.setup(SIZE + 50, SIZE + 50)
SCREEN.bgcolor("black")

food = turtle.Turtle()
food.up()
food.shape("circle")
food.color("red")
food.ht()


def getRandPos():
    return (randint(-SIZE//2, SIZE//2), randint(-SIZE//2, SIZE//2))


food_coor = getRandPos()

had = turtle.Turtle()
had.up()
had.shape("square")
had.color("green")
had.ht()

had_coor = [(0, 0)]

stamps = []

dir_x = 0
dir_y = 0

stop = False


def aktualizuj_display():
    tracer = SCREEN.tracer()
    SCREEN.tracer(0)
    
    food.clearstamps(1)
    had.clearstamps(len(had_coor))
    
    food.goto(food_coor[0], food_coor[1])
    food.stamp()

    for x, y in had_coor:
        had.goto(x, y)
        had.stamp()
    
    SCREEN.tracer(tracer)
    

def pozice():
    global had_coor, food_coor, stop
    avance()
    if narazdohada() or narazdosteny():
        stop = True
    if jezeni():
        append()
        food_coor = getRandPos() 


def smyčka():
    if stop:
        Konec_hry()
        return
    pozice()
    aktualizuj_display()
    SCREEN.ontimer(smyčka, 100)
  
    
def narazdohada():
    global had_coor
    return len(set(had_coor))<len(had_coor)


def narazdosteny():
    x, y = had_coor[0]
    return not (-SIZE//2-50<x<SIZE//2+50) or not (-SIZE//2-50<y<SIZE//2+50)    


def jezeni():
    sx, sy = had_coor[0]
    fx, fy = food_coor
    distance = ((sx-fx)**2 + (sy-fy)**2)**.5
    return distance<20


def append():
    global had_coor
    a = had_coor[-1][:]
    had_coor.append(a)


def setDir(x, y):
    global dir_x, dir_y
    dir_x = x
    dir_y = y
    
    
def avance():
    global had_coor
    x, y = had_coor[0]
    x += dir_x*20
    y += dir_y*20
    had_coor.insert(0, (x, y))
    had_coor.pop(-1)
    
def right(): setDir(1, 0)
def left(): setDir(-1, 0)
def up(): setDir(0, 1)
def down(): setDir(0, -1)
    

def Konec_hry():
    d = turtle.Turtle()
    d.up()
    d.ht()
    d.color("red")
    d.write("GAME OVER\nBODY : %04d" % (len(had_coor)), align="center", font=("Arial Black", 40, "bold"))
    SCREEN.onclick(lambda*a:[SCREEN.bye(),exit()])


SCREEN.onkeypress(up, "Up")
SCREEN.onkeypress(down, "Down")
SCREEN.onkeypress(right, "Right")
SCREEN.onkeypress(left, "Left")
SCREEN.listen()
smyčka()
turtle.mainloop()