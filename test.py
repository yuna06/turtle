from turtle import *
import random
color('red', 'yellow')
begin_fill()

list = []
x = 1
y = 2
pos11 = (x, y)
list.append(pos11)
print(list)
goto(pos11)

d = dict()
d["pos12"] = (100,100)
d["pos13"] = (200,200)
print(d)

# 動的に生成するとしたら
for i, s in enumerate(["'ほげ'","'ふが'", "'ぴよ'"]):
    exec(f"string{i+1} = {s}")
    exec(f"print(string{i+1})")

end_fill()
done()
