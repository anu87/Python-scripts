# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:27:39 2016

Classroom code for turtle to learn python programmin
"""

import turtle

wn = turtle.Screen() #creates the background screen
wn.bgcolor('purple')
wn.title('The Sandbox')
wn.setup(500,500)

#setting the name -> 1st create a variable named george
george = turtle.Turtle()

george.shape('turtle')

george.forward(100)

george.left(90)

george.forward(50)

george.left(90)

george.forward(100)

george.left(90)

george.forward(50)

#triangle

#george.left(180)
#george.forward(200)
#george.left(120)
#george.forward(200)
#george.left(120)
#george.forward(200)

#change color for each line using for loop

#colors = ['red', 'yellow', 'blue'] # this data format is a list in ''
#for color in colors:
 #   george.color(color)
  #  george.forward(50)
   # george.left(120)

#write a fn to draw triangle w just one colour

def draw_triangle(draw_color):
    for side in range(3):
        george.color(draw_color)
        george.forward(50)
        george.left(120)
        
draw_triangle('green') # here draw_color is defined as green
george.penup()
george.right(45)
george.pendown()

draw_triangle('red')

wn.mainloop() # wn - window - keeps the window open till the user closes it 
# or the window will close automatically after running the program



print ('hello world')

