from turtle import *
from math import *

speed(0)
boja = ['#C1133D', '#001C5A','white']
showturtle()

a = 0
b = 0
m = 0
n = 0
x=30*sin(radians(38))/sin(radians(71))
pomak = 30 + x/2

def trokut():
  pu()
  goto(-500,-10)
  fd(250)
  fd(380)
  pd()
  color(boja[1])

  begin_fill()
  krak = (500+380)/(sin(radians(65)))
  lt(155)
  fd(krak)
  global a
  global b
  a = xcor()
  b = ycor()
  lt(115)
  fd(cos(radians(65))*krak*2)
  lt(115)
  fd(krak)
  lt(65)

  end_fill()
    
def zvijezda(stranica, kut):
  begin_fill()
  for x in range(5):
    fd(stranica)
    rt(kut)
    fd(stranica)
    lt(72+kut)
  end_fill()

def kruznica1():
  color(boja[2])
  begin_fill()
  circle(120)
  end_fill()

def kruznica2():
  color(boja[0])
  begin_fill()
  circle(90)
  end_fill()

def traka1():
  begin_fill()
  fd(1400)
  rt(80)
  rt(60)
  fd(100)
  rt(40)
  fd(1082)
  rt(15)
  fd(250)
  end_fill()

def traka2():
  begin_fill()
  lt(90)
  lt(10)
  fd(1400)
  lt(80)
  lt(60)
  fd(100)
  lt(40)
  fd(1082)
  lt(15)
  fd(250)
  end_fill()

def traka3():
  begin_fill()
  fd(100)
  setheading(180)
  goto(23,40)
  lt(155)
  fd(118)
  rt(130)
  fd(118)
  setheading(0)
  goto(339.07+50*sqrt(3),ycor())
  setheading(150)
  fd(100)
  end_fill()

def first_stars():
  for x in range(12):
    if(x!=8 and x!=10):
      zvijezda(30,70)
    pu()
    fd(pomak)
    if x == 1:
      global m
      global n
      m = xcor()
      n = ycor()
    circle(200,30)
    rt(180)
    fd(pomak)
    lt(180)
    pd()

def second_stars():
  for x in range(18):
    if(x==1 or x==2 or x==7 or x==8 or x==13 or x==14):
      zvijezda(30,70)
    pu()
    fd(pomak)
    circle(320,20)
    rt(180)
    fd(pomak)
    lt(180)
    pd()
    
def third_star():
  for x in range(36):
    if(x==27):
      zvijezda(30,70)
    pu()
    fd(pomak)
    circle(440,10)
    rt(180)
    fd(pomak)
    lt(180)
    pd()

trokut()

setheading(0)
goto(-500,-130)
kruznica1()

goto(-500,-100)
kruznica2()

color(boja[2])
goto(-500,-130)

setheading(180)
pu()
goto(-500+pomak,190)
pd()

first_stars()

pu()
rt(90)
fd(120)
lt(90)
pd()

second_stars()

pu()
rt(90)
fd(120)
lt(90)
pd()

third_star()

pu()
color(boja[0])
goto(a,b)
begin_fill()
rt(180)
rt(10)
pd()

traka1()

color(boja[1])
lt(115)
fd(2*abs(b)+20)
color(boja[0])

traka2()

pu()
setheading(30)
goto(339.07,-10);
pd()


traka3()


