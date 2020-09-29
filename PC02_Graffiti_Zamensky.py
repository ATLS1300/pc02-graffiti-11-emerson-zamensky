#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightblue")
panel.bgpic(image)

# sqaure above left shoulder 
up()
goto(-250,-14)
down()
speed(20)
pensize(4)
pencolor("black")
fillcolor(230, 10, 100)
begin_fill()
for b in range(4):
    forward(50)
    left(90)
end_fill()

# star and circle at end of star
up()
goto(-205, 110)
down()

pensize(5)
pencolor("purple")
for i in range(20):
    forward(i * 10)
    right(144)
pencolor('orange')
circle(20)

# sunglasses bridge
pencolor('black')
up()
goto(0, 120)
left(11)
down()
forward(27)
up()
# sunglasses ear piece 
goto(-34, 113)
right(195)
down()
forward(54)
up()
# sunglasses lenses
goto(45, 137)
down()
fillcolor('black')
begin_fill()
circle(18)
end_fill()
up()
goto(-15, 136)
down()
fillcolor('black')
begin_fill()
circle(18)
end_fill()

# sun
up()
goto(288, 148)
color('yellow')
down()
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#sorry it's kind of random, I wanted to do something with a dollar sign but couldn't figure that out so I thought a sun and sunglasses were fun with some other cool designs! 
