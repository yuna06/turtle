from turtle import *
import random
import numpy as np

speed(5)
width(2)
colormode(255)

def add(x, y):
    z0 = x[0] + y[0]
    z1 = x[1] + y[1]
    z = (z0, z1)
    goto(z)

def tri(x,y,z,a,b,c):
    if random.randint(1,11)<=5:
        fill = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        line = fill
    else:
        line = 'gray'
        fill = 'white'
    color(line, fill)
    print("color is " + str(color()))
    begin_fill()
    add(x,a)
    pendown()
    add(y,b)
    add(z,c)
    add(x,a)
    penup()
    end_fill()

def squ(w,x,y,z,a,b,c,d):
    if random.randint(1,11)<=5:
        fill = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        line = fill
    else:
        line = 'gray'
        fill = 'white'
    color(line, fill)
    begin_fill()
    add(w,a)
    pendown()
    add(x,b)
    add(y,c)
    add(z,d)
    add(w,a)
    penup()
    end_fill()

pos0 = (0,80)
pos1 = (80,160)
pos2 = (160,80)
pos3 = (200,40)
pos4 = (160,-60)
pos5 = (0,-160)
pos6 = (-60,-120)
pos7 = (-140,-50)
pos8 = (-200,40)
pos9 = (-80,160)
pos10 = (-40,120)
bool = True

pos11 = (40,40)
pos12 = (160,40)
pos13 = (-80,120)
pos14 = (-120,40)
pos15 = (-80,40)
pos16 = (-40,40)
pos17 = (-20,40)
pos18 = (-100,-40)
pos19 = (0,-40)

pos20 = (20,-100)
pos21 = (70,-100)
pos22 = (90,-40)
pos23 = (120,-60)
pos24 = (100,-30)
pos25 = (90,0)
pos26 = (10,-70)

while True:
    penup()

    tri(pos0,pos1,pos2,(0,3),(0,0),(-4,3))
    squ(pos2,pos3,pos11,pos0,(4,-3),(0,3),(4,3),(6,-3))
    tri(pos3,pos4,pos12,(0,-3),(3,3),(3,-3))
    tri(pos11,pos4,pos12,(9,-3),(-3,3),(-3,-3))

    tri(pos9,pos13,pos10,(3,0),(3,3),(-3,3))
    tri(pos9,pos8,pos15,(-3,-3),(0,3),(-3,3))
    squ(pos13,pos10,pos16,pos15,(3,-3),(-6,-3),(-6,3),(3,3))
    tri(pos10,pos16,pos17,(-3,-3),(-3,3),(-3,3))

    tri(pos8,pos7,pos14,(0,-3),(-3,3),(-3,-3))
    tri(pos14,pos7,pos18,(0,-3),(3,3),(-3,3))
    squ(pos14,pos18,pos19,pos17,(3,-3),(0,6),(-3,6),(-3,-3))
    tri(pos7,pos6,pos18,(0,-3),(-3,-3),(-3,-3))
    tri(pos18,pos6,pos5,(3,-3),(0,-3),(-6,-3))
    tri(pos18,pos5,pos19,(6,0),(0,0),(-3,0))

    tri(pos10,pos26,pos25,(3,-3),(3,0),(-3,-3))
    squ(pos26,pos20,pos24,pos25,(3,-6),(0,3),(-3,0),(-3,-9))
    tri(pos19,pos5,pos20,(3,-12),(3,0),(-3,-3))
    squ(pos20,pos5,pos21,pos22,(0,-3),(3,3),(-3,3),(-3,-3))
    tri(pos5,pos4,pos21,(9,6),(-3,-3),(0,-3))
    tri(pos22,pos21,pos23,(3,-3),(3,6),(-3,-12))
    tri(pos22,pos23,pos24,(3,3),(-3,-9),(0,-3))
    tri(pos25,pos23,pos4,(6,-9),(3,-9),(-3,0))

    goto(1000,1000)

done()
