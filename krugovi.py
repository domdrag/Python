

from turtle import *
speed(1)
def a(n,d):
    if n>0:
        for i in range(2):
            circle(d,180)
            a(n-1,d//2)
print(a(5,100))


