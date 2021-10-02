from turtle import *
hideturtle()
speed(0)
def a(n,d):
    if n>0:
        for i in range(4):
            fd(d)
            lt(90)
            a(n-1,d//3)
            
print(a(4,250))

