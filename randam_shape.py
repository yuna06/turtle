from turtle import *
import random
import numpy as np
import math

speed(5)
width(2)
colormode(255)

def add(x, y):
    z0 = x[0] + y[0]
    z1 = x[1] + y[1]
    z = (z0, z1)
    goto(z)

def collision(x,y):
    if (-200<x<-80 and y<x+240 and y>-x-160) or \
    (-80<=x<0 and y<-x+80 and y>-x-160) or \
    (0<=x<80 and y<x+80 and y>0.625*x-160) or \
    (80<=x<160 and y<-x+240 and y>0.625*x-160) or \
    (160<=x<200 and y<-x+240 and y>2.5*x-460):
        return True
    else:
        return False

# instance random square.
def r_squ():
    x = random.randint(-200,200)
    y = random.randint(-160,160)
    a = random.randint(50,200)
    b = random.randint(50,200)
    alpha = math.radians(random.randint(0,180))
    beta = math.radians(random.randint(0,180))
    p = (x+a*math.cos(alpha),y+a*math.sin(alpha))
    q = (x+b*math.cos(beta),y+b*math.sin(beta))
    r = (x-a*math.cos(alpha),y-a*math.sin(alpha))
    s = (x-b*math.cos(beta),y-b*math.sin(beta))
    list = [p,q,r,s]
    return list


def tri():
    bool = True
    while bool:
        x = random.randint(-200,200)
        y = random.randint(-160,160)
        a = random.randint(50,200)
        b = random.randint(50,200)
        alpha = math.radians(random.randint(0,180))
        beta = math.radians(random.randint(0,180))
        p = (x+a*math.cos(alpha),y+a*math.sin(alpha))
        q = (x+b*math.cos(beta),y+b*math.sin(beta))
        r = (x-a*math.cos(alpha),y-a*math.sin(alpha))
        s = (x-b*math.cos(beta),y-b*math.sin(beta))
        if collision(p[0],p[1]) and \
        collision(q[0],q[1]) and \
        collision(r[0],r[1]) and \
        collision(s[0],s[1]):
            bool = False
        else:
            x = random.randint(-200,200)
            y = random.randint(-160,160)
            a = random.randint(50,200)
            b = random.randint(50,200)
            alpha = math.radians(random.randint(0,180))
            beta = math.radians(random.randint(0,180))
            p = (x+a*math.cos(alpha),y+a*math.sin(alpha))
            q = (x+b*math.cos(beta),y+b*math.sin(beta))
            r = (x-a*math.cos(alpha),y-a*math.sin(alpha))
            s = (x-b*math.cos(beta),y-b*math.sin(beta))

    # color
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



def squ(posx):
    # instance coordicate of square which contain one outpoint
    if random.randint(1,2)==1:
        bool = True
        while bool:
            a = random.randint(40,120)
            b = a + random.randint(-20,-20)
            alpha = math.radians(random.randint(0,360))
            beta = math.radians(random.randint(0,360))
            p = posx
            q = (posx[0]-round(a*math.cos(alpha)),posx[1]-round(a*math.sin(alpha)))
            r = (posx[0]-round(a*math.cos(alpha))-round(b*math.cos(beta)),posx[1]-round(a*math.sin(alpha))-round(b*math.sin(beta)))
            s = (posx[0]-round(b*math.cos(beta)),posx[1]-round(b*math.sin(beta)))
            x = posx[0]-(round(a*math.cos(alpha))-round(b*math.cos(beta)))/2
            y = posx[1]-(round(a*math.sin(alpha))-round(b*math.sin(beta)))/2

            if collision(q[0],q[1]) and \
            collision(r[0],r[1]) and \
            collision(s[0],s[1]):
                boolean = True
                if a>b:
                    long = a
                else:
                    long = b
                if points==[]:
                    points.append([x,y,long,p,q,r,s])
                    bool = False
                else:
                    b_list = []
                    for i in range(len(points)):
                        b_list.append(math.sqrt(((x-points[i][0])**2)+((y-points[i][1])**2)) > long+points[i][2]-20)
                    print(b_list)
                    for i in b_list:
                        boolean = boolean and i
                    if boolean:
                        points.append([x,y,long,p,q,r,s])
                        bool = not boolean
                    else:
                        bool = True
            else:
                bool = True
    # instance coordicate of square which dont contain one outpoint
    else:
        bool = True
        while bool:
            x = random.randint(-200,200)
            y = random.randint(-160,160)
            a = random.randint(40,120)
            b = a + random.randint(-20,-20)
            alpha = math.radians(random.randint(0,180))
            beta = math.radians(random.randint(0,180))
            p = (x+round(a*math.cos(alpha)),y+round(a*math.sin(alpha)))
            q = (x+round(b*math.cos(beta)),y+round(b*math.sin(beta)))
            r = (x-round(a*math.cos(alpha)),y-round(a*math.sin(alpha)))
            s = (x-round(b*math.cos(beta)),y-round(b*math.sin(beta)))

            if collision(p[0],p[1]) and \
            collision(q[0],q[1]) and \
            collision(r[0],r[1]) and \
            collision(s[0],s[1]):
                boolean = True
                if a>b:
                    long = a
                else:
                    long = b
                if points==[]:
                    points.append([x,y,long,p,q,r,s])
                    bool = False
                else:
                    b_list = []
                    for i in range(len(points)):
                        b_list.append(math.sqrt((x-points[i][0])**2+(y-points[i][1])**2) > long+points[i][2]-20)
                    print(b_list)
                    for i in b_list:
                        boolean = boolean and i
                    if boolean:
                        points.append([x,y,long,p,q,r,s])
                        bool = not boolean
                    else:
                        bool = True
            else:
                bool = True
    # color
    if random.randint(1,11)<=5:
        fill = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        line = fill
    else:
        line = 'gray'
        fill = 'white'
    color(line, fill)
    begin_fill()
    goto(p)
    pendown()
    goto(q)
    goto(r)
    goto(s)
    goto(p)
    penup()
    end_fill()

list = [pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10]
x = 0

# while True:
penup()
# or i in list
for i in list:
    if x >= 9:
        x =0
    x += 1

    goto(i)
    pendown()
goto(pos0)
penup()
points = []
for i in np.arange(5):
    posx = list[random.randint(0,10)]
    squ(posx)
# print(points)
p_list = []
for i in range(len(points)):
    for j in range(3,7):
        p_list.append(points[i][j])
print(p_list)
goto(1000,1000)

done()
