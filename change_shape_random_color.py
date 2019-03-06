from turtle import *
import random
import numpy as np



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

def fluc():
    # return random.randint(30,60)
    return 0
# y = (y1-y0)/(x1-x0)*(x-x0)+y0
# x = (x1-x0)/(y1-y0)*(y-y0)+x0
"""
def line1(y):
    return (pos20[0]-pos10[0])/(pos20[1]-pos10[1])*(y-pos10[1])+pos10[0]

def line2(y):
    return (pos4[0]-pos0[0])/(pos4[1]-pos0[1])*(y-pos0[1])+pos0[0]
"""
"""
-80<a<0
-120<b<-80
-60<c<40
0<d<30
-160<e<c
d<f<30
"""

while True:
    speed(7)
    width(2)
    colormode(255)
    a = random.randint(-80,0)
    b = random.randint(-120,-80)
    c = random.randint(-60,40)
    d = random.randint(0,30)
    e = random.randint(-16,40)
    f = random.randint(d,30)
    g = random.randint(-200,-80)


    pos0 = (0,80)
    pos1 = (80,160)
    pos2 = (160,80)
    pos3 = (200,40)
    pos4 = (140,-60)
    pos5 = (0,-160)
    pos6 = (-60,-120)
    pos7 = (-140,-50)
    pos8 = (-200,40)
    pos9 = (-80,160)
    pos10 = (a,-a+80)
    bool = True

    pos11 = ((pos4[0]-pos0[0])/(pos4[1]-pos0[1])*(pos3[1]-pos0[1])+pos0[0],pos3[1])
    pos12 = (pos4[0],pos3[1])
    pos13 = (pos9[0],pos10[1])
    pos14 = (g,pos8[1])
    pos15 = (pos9[0],pos8[1])
    pos16 = (a,pos8[1])
    pos17 = ((d-pos10[0])/(e-pos10[1])*(40-pos10[1])+pos10[0],pos8[1])
    pos18 = (b,c)
    pos19 = ((d-pos10[0])/(e-pos10[1])*(c-pos10[1])+pos10[0],c)

    pos20 = (d,e)
    pos21 = (70+fluc(),-100+fluc())
    pos22 = (90,-40)
    pos23 = (120,-60)
    pos24 = (100,-30)
    pos25 = (90,0)
    pos26 = ((pos20[0]-pos10[0])/(pos20[1]-pos10[1])*(f-pos10[1])+pos10[0],f)
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
    reset()

done()
