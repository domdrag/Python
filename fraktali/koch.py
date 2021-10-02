from turtle import *

speed(0)
penup()
setx(250)
sety(-150)
pendown()

rt(180)
def prva_iter(d):
    fd(d)
    lt(60)
    fd(d)
    rt(120)
    fd(d)
    lt(60)
    fd(d)

def koch(n,d):
    if n>1:
        koch(n-1,d)
        lt(60)
        koch(n-1,d)
        rt(120)
        koch(n-1,d)
        lt(60)
        koch(n-1,d)
    else:
        prva_iter(d)

for i in range(3):
    koch(4,7)
    rt(120)



