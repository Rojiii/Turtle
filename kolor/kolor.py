from turtle import *
import colorsys

speed(0)
hideturtle()
bgcolor('black')
tracer(5)
width(2)
s = 1
v = 1
h = 0.0

for i in range(90):
    color(colorsys.hsv_to_rgb(h, s, v))
    forward(60)
    right(120)
    circle(60)
    left(240)
    forward(60)
    left(60)
    forward(60)
    h += 0.2
    color(colorsys.hsv_to_rgb(h, s, v))
    forward(60)
    right(60)
    forward(60)
    right(60)
    forward(60)
    left(120)
    circle(-60)
    right(240)
    forward(60)
    right(60)
    forward(60)
    left(2)
    h += 0.02

done()