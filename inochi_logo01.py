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
"""
def go(i):
    goto list[i]
"""

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

"""
# list1 = [pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19]
x = random.uniform(pos1[0], pos2[0])
y = random.uniform(pos1[1], pos2[1])

while bool:
    if x + y < 80:
        x = random.uniform(pos1[0], pos2[0])
        y = random.uniform(pos1[1], pos2[1])
    else:
        bool = False

pos11 = (x, y)
goto(pos11)
print(pos())
goto(pos0)
print(pos())
"""


for i, s in enumerate(np.array(range(10))):
    print(s)
    print(i)
    exec(f"x = random.uniform(pos{i+0}[0], pos{i+1}[0])")
    exec(f"y = random.uniform(pos{i+0}[1], pos{i+1}[1])")

    while bool:
        if exec(f"y > (((pos{i+1}[1]-pos{i+0}[1]) / (pos{i+1}[0]-pos{i+0}[0])) * (x-pos{i+0}[0])) + pos{i+0}[1]"):
            exec(f"x = random.uniform(pos{i+0}[0], pos{i+1}[0])")
            exec(f"y = random.uniform(pos{i+0}[1], pos{i+1}[1])")
        else:
            bool = False

    exec(f"pos{i+10} = (x, y)")
    exec(f"goto(pos{i+10})")
    exec(f"print(pos())")
    exec(f"goto(pos{i+1})")
    exec(f"print(pos())")

end_fill()
done()
