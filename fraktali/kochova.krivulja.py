from turtle import *


pu()
setx(-300)
sety(-100)
pd()
speed(0)
def a(n,d):
    if n>0:
        a(n-1,d)
        fd(d)
        lt(60)
        a(n-1,d)
        fd(d)
        rt(120)
        a(n-1,d)
        fd(d)
        lt(60)
        a(n-1,d)


def b(n,d):
    if n>0:
        b(n-1,d)
        lt(60)
        b(n-1,d)
        rt(120)
        b(n-1,d)
        lt(60)
        b(n-1,d)
        
    if n==0:
        fd(d)
        lt(60)
        fd(d)
        rt(120)
        fd(d)
        lt(60)
        fd(d)

b(4,10)
    
update()
mainloop()



