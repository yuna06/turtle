from turtle import *
import random
import numpy as np
color('red')
begin_fill()

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

goto(pos2)
goto(pos3)
goto(pos11)
goto(pos0)
goto(pos11)
goto(pos4)
goto(pos12)

penup()
goto(pos11)
goto(pos9)
pendown()

goto(pos13)
goto(pos10)
goto(pos17)
goto(pos16)
goto(pos10)
goto(pos13)
goto(pos15)
goto(pos16)
goto(pos15)
goto(pos13)
goto(pos15)
goto(pos8)
goto(pos14)
goto(pos18)
goto(pos19)
goto(pos17)

penup()
goto(pos14)
pendown()

goto(pos7)
goto(pos18)
goto(pos6)
goto(pos18)
goto(pos5)
goto(pos19)

goto(pos20)
goto(pos5)
goto(pos21)
goto(pos23)
goto(pos4)
goto(pos24)
goto(pos25)
goto(pos26)
goto(pos20)
goto(pos22)
goto(pos21)
goto(pos23)
goto(pos22)
goto(pos24)
goto(pos23)
end_fill()
done()
