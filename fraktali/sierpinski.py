from turtle import *
hideturtle()
speed(0)
def a(n,d):
    if n>0:
        for i in range(3):
            fd(d)
            lt(120)
            a(n-1,d//2)
            
print(a(4,250))
