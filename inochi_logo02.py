from turtle import *
import random
import numpy as np
color('red', 'yellow')
begin_fill()

pos0 = (0,80)
pos1 = (80,160)
pos2 = (160,80)
pos3 = (200,50)
pos4 = (160,-60)
pos5 = (0,-160)
pos6 = (-60,-120)
pos7 = (-120,-50)
pos8 = (-200,50)
pos9 = (-80,160)
pos10 = (-40,120)
bool = True


list = [pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10]
print(list[0])
print(pos1[1])
x = 0

# while True:
penup()
# or i in list
for i in list:
    if x >= 9:
        x =0
    x += 1
    print(x)
    goto(i)
    pendown()
    print(pos())
goto(pos0)

# if random.randrange(2)=0:
    # pos11 = ()



end_fill()
done()
