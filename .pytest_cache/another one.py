""" 
Name: Emma Boutoille 
Date: September 17 
S2.1 Turtle Lines
Assignment 2.1 Turtle Art
"""     

# ---------------- Imports --------------------

import turtle # import turtle library
import time # import time library

# ------------------- Window Setup ----------------
# New section to setup our screen for graphics

wn = turtle.Screen() # create window called wn
wn.setup(height=600, width=800) # set window size
wn.title("A2.1 Turtle Art") # Window title
wn.bgcolor("sky blue") # set background colour to sky blue

# -------------------  Turtle Setup -------------------------
# Create turtle
# Create zoey
zoey = turtle.Turtle() # creates a turtle called zoey

# Set turtle properties
zoey.width(6) # sets the line width that zoey will draw equal to 6
zoey.speed(10) # sets zoey to speed 2
zoey.color("red") # set zoey's color to red
zoey.shape("turtle") # set zoey to a turtle
zoey.ht() # hide zoey

# Create a pen turtle to write
pen = turtle.Turtle() # create a turtle called pen to write text on the screen
pen.ht() # hide pen
penstyle_welcome_sign = ("Arial", 12) # set the text font and size to Arial size 12
penstyle_house_number = ("Arial", 10, "bold") # set the text font, size, and style to Arial size 12 bold
penstyle_goodbye_message = ("Arial", 20) # set the text font and size to Arial size 20

# -------------------------  Functions -------------------
def tree_trunk(): # create a function used to draw the triangle tree trunks
  zoey.color("brown") # set zoey's color to brown
  zoey.fillcolor("brown") # tell zoey to fill shape in the color brown
  zoey.begin_fill() # zoey begins to fill shape
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(50) # move zoey forward 50
  zoey.lt(90) # rotate zoey to the left by 90 degrees
  zoey.fd(25) # move zoey forward 25
  zoey.lt(90) # rotate zoey to the left by 90 degrees
  zoey.fd(50) # move zoey forward 50
  zoey.end_fill() # zoey stops filling shape
  zoey.ht() # hide zoey

def right_side_of_tree(): # create a function used to draw the right side of the triangle trees
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(90) # move zoey forward 90
  zoey.lt(115) # rotate zoey to the left by 115 degrees
  zoey.fd(50) # move zoey forward 50 
  zoey.rt(115) # rotate zoey to the right by 115 degrees
  zoey.fd(10) # move zoey forward 10
  zoey.lt(115) # rotate zoey to the left by 115 degrees
  zoey.fd(45) # move zoey forward 45
  zoey.rt(115) # rotate zoey to the right by 115 degrees
  zoey.fd(5) # move zoey forward 5
  zoey.lt(115) # rotate zoey to the left by 115 degrees
  zoey.fd(45) # move zoey forward 45
  zoey.lt(115) # rotate zoey to the left by 115 degrees
  zoey.ht() # hide zoey

def left_side_of_tree(): # create a function used to draw the left side of the traingle trees
  zoey.st() # show turtle
  zoey.pd() # put pen down
  zoey.rt(165) # rotate zoey to the right by 165 degrees
  zoey.fd(50) # move zoey forward 50
  zoey.lt(115) # rotate zoey to the left by 115 degrees
  zoey.fd(10) # move zoey forward 10
  zoey.rt(115) # rotate zoey to the right by 115 degrees
  zoey.fd(45) # move zoey forward 45
  zoey.lt(115) # rotate zoey to the left by 115 degrees
  zoey.fd(5) # move zoey forward 5
  zoey.rt(115) # rotate zoey to the right by 115 degrees
  zoey.fd(45) # move zoey forward 45
  zoey.ht() # hide zoey

def bricks1(): # create a function used to draw the horizontal lines of the bricks
  zoey.color("red") # set zoey's color to red
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(138) # move zoey forward 138
  zoey.ht() # hide zoey

def bricks2(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(27) # move zoey forward 27
  zoey.ht() # hide zoey

def bricks3(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(18) # move zoey forward 18
  zoey.ht() # hide zoey

def bricks4(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(29) # move zoey forward 29
  zoey.ht() # hide zoey

def bricks5(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(368) # move zoey forward 368
  zoey.ht() # hide zoey

def bricks6(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(62) # move zoey forward 62
  zoey.ht() # hide zoey

def bricks7(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(110) # move zoey forward 110
  zoey.ht() # hide zoey

def bricks8(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(83) # move zoey forward 83
  zoey.ht() # hide zoey

def bricks9(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(59) # move zoey forward 59
  zoey.ht() # hide zoey

def bricks10(): # create a function used to draw the horizontal lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(30) # move zoey forward 30
  zoey.ht() # hide zoey

def divide_bricks(): # create a function used to draw the vertical lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(25) # move zoey forward 25
  zoey.ht() # hide zoey

def divide_bricks2(): # create a function used to draw the vertical lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(20) # move zoey forward 20
  zoey.ht() # hide zoey

def divide_bricks3(): # create a function used to draw the vertical lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(18) # move zoey forward 18
  zoey.ht() # hide zoey

def divide_bricks4(): # create a function used to draw the vertical lines of the bricks
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(10) # move zoey forward 10
  zoey.ht() # hide zoey

def sun_rays():
  zoey.rt(45) # rotate zoey to the right by 45 degrees
  zoey.st() # show zoey
  zoey.pd() # put pen down
  zoey.fd(30) # move zoey forward 30
  zoey.ht() # hide zoey

# ---------------------- Main Program --------------------
# Drawing With Zoey
# Drawing The House Walls
zoey.pu() # lift pen up
zoey.goto(-183,-19) # move zoey to -183,-19
zoey.fillcolor("white") # tell zoey to fill shape in the color white
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(270) # move zoey forward 270
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.fd(370) # move zoey forward 370
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.fd(270) # move zoey forward 270
zoey.end_fill() # zoey stops filling shape
zoey.width(3) # sets the line width that zoey will draw equal to 3
zoey.ht() # hide zoey

# Drawing The Roof
zoey.pu() # lift pen up
zoey.goto(-200,-35) # move zoey to -200,-35
zoey.color("black") # set zoey's color to black
zoey.fillcolor("black") # tell zoey to fill shape in the color black
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.rt(45) # rotate zoey to the right by 45 degrees
zoey.fd(285) # move zoey forward 285
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(285) # move zoey forward 285
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.fd(25) # move zoey forward 25
for i in range (2): # create a for loop that repeats the code twice
  zoey.lt(90) # rotate zoey to the left by 90 degrees
  zoey.fd(310) # move zoey forward 310
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.fd(25) # move zoey forward 25
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The White Triangle To Fill The Top of The House
zoey.pu() # lift pen up
zoey.color("white") # set zoey's color to white
zoey.fillcolor("white") # tell zoey to fill shape in the color white
zoey.begin_fill() # zoey begins to fill shape
zoey.goto(-181,-19) # move zoey to -181,-19
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.fd(260) # move zoey forward 260
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(260) # move zoey forward 260
zoey.rt(135) # rotate zoey to the right by 135 degrees
zoey.fd(370) # move zoey forward 370
zoey.rt(225) # rotate zoey to thr right by 225 degrees
zoey.end_fill() # zoey stops filling shape

# Drawing The Top Window Pane
zoey.pu() # lift pen up
zoey.goto(-45,92) # move zoey to -45,92
zoey.color("grey") # set zoey's color to grey
zoey.fillcolor("grey") # tell zoey to fill shape in the color grey
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # pen down
zoey.lt(45) # rotate zoey to the left by 45 degrees
for i in range (3): # create a for loop that repeats the code three times
  zoey.fd(90) # move zoey forward 90
  zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(90) # move zoey forward 90
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Top Left Hand Corner of The Top Window Pane
zoey.pu() # lift pen up
zoey.goto(-35,82) # move zoey to -35,82
zoey.color("sky blue") # set zoey's color to sky blue
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Top Right Hand Corner of The Top Window Pane
zoey.pu() # lift pen up
zoey.goto(5,82) # move zoey to 5,82
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Bottom Left Hand Corner of The Top Window Pane
zoey.pu() # lift pen up
zoey.goto(-35,42) # move zoey to -35,42
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Bottom Right Hand Corner of The Top Window Pane
zoey.pu() # lift pen up
zoey.goto(5,42) # move zoey to 5,42
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Trapezoid Shaped Roof
zoey.pu() # lift pen up
zoey.goto(-154,-76) # move zoey to -154,-76
zoey.color("black") # set zoey's color to black
zoey.fillcolor("black") # tell zoey to fill shape in the color black
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.rt(50) # rotate zoey to the right by 50 degrees
zoey.fd(70) # move zoey forward 70
zoey.rt(40) # rotate zoey to the right by 40 degrees
zoey.fd(200) # move zoey forward 200
zoey.rt(40) # rotate zoey to the right by 40 degrees
zoey.fd(70) # move zoey forward 70
zoey.end_fill() # zoey stops filling shape
zoey.rt(50) # rotate zoey to the right by 50 degrees
zoey.fd(10) # move zoey forward 10
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(307) # move zoey forward 307
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(10) # move zoey forward 10
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(307) # move zoey forward 307
zoey.ht() # hide zoey

# Drawing The Bottom Left Window Pane
zoey.pu() # lift pen up
zoey.goto(-154,-110) # move zoey to -154,-110
zoey.color("grey") # set zoey's color to grey
zoey.fillcolor("grey") # tell zoey to fill shape in the color grey
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (3): # create a for loop that repeats the code three times
  zoey.fd(90) # move zoey forward 90
  zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(90) # move zoey forward 90
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Top Left Hand Corner of The Bottom Left Window Pane
zoey.pu() # lift pen up
zoey.goto(-144,-120) # move zoey to -144,-120
zoey.color("sky blue") # set zoey's color to sky blue
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Top Right Hand Corner of The Bottom Left Window Pane
zoey.pu() # lift pen up
zoey.goto(-104,-120) # move zoey to -104,-120
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Bottom Left Hand Corner of The Bottom Left Window Pane
zoey.pu() # lift pen up
zoey.goto(-144,-160) # move zoey to -144,-160
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Bottom Right Hand Corner of The Bottom Left Window Pane
zoey.pu() # lift pen up
zoey.goto(-104,-160) # move zoey to -104,-160
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Bottom Right Window Pane
zoey.pu() # lift pen up
zoey.goto(63,-110) # move zoey to 63,-110
zoey.color("grey") # set zoey's color to grey
zoey.fillcolor("grey") # tell zoey to fill shape in the color grey
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(90) # move zoey forward 90
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Top Left Hand Corner of The Bottom Right Window Pane
zoey.pu() # lift pen up
zoey.goto(73,-120) # move zoey to 73,-120
zoey.color("sky blue") # set zoey's color to sky blue
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Top Right Hand Corner of The Bottom Right Window Pane
zoey.pu() # lift pen up
zoey.goto(113,-120) # move zoey to 113,-120
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Bottom Left Hand Corner of The Bottom Right Window Pane
zoey.pu() # lift pen up
zoey.goto(73,-160) # move zoey to 73,-160
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Individual Window in The Bottom Right Hand Corner of The Bottom Right Window Pane
zoey.pu() # lift pen up
zoey.goto(113,-160) # move zoey to 113,-160
zoey.fillcolor("sky blue") # tell zoey to fill shape in the color sky blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
for i in range (4): # create a for loop that repeats the code four times
  zoey.rt(90) # rotate zoey to the right by 90 degrees
  zoey.fd(30) # move zoey forward 30
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Outside Rectangle of The Door
zoey.pu() # lift pen up
zoey.goto(-44,-286) # move zoey to -44,-286
zoey.color("brown") # set zoey's color to brown
zoey.fillcolor("brown") # tell zoey to fill shape in the color brown
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.fd(136) # move zoey forward 136
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(88) # move zoey forward 88
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(136) # move zoey forward 136
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Inside Rectangle of The Door
zoey.pu() # lift pen up
zoey.goto(-34,-286) # move zoey to -34,-286
zoey.color("navy blue") # set zoey's color to navy blue
zoey.fillcolor("navy blue") # tell zoey to fill shape in the color navy blue
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.rt(180) # rotate zoey to the right by 180 degrees
zoey.fd(126) # move zoey forward 126
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(68) # move zoey forward 68
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(126) # move zoey forward 126
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Door Handle
zoey.pu() # lift pen up
zoey.goto(12,-226) # move zoey to 12,-226
zoey.color("gold") # set zoey's color to gold
zoey.fillcolor("gold") # tell zoey to fill shape in the color gold
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(7) # print circle with a radius of 7
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing the triangle tree located on the left side of the house
zoey.pu() # lift pen up
zoey.goto(-330,-238) # move zoey to -330,-238
tree_trunk() # call on function tree_trunk

zoey.pu() # lift pen up
zoey.goto(-360,-238) # move zoey to -360,-238
zoey.width(10) # sets the line width that zoey will draw equal to 10
zoey.color("green") # set zoey's color to green
zoey.fillcolor("green") # tell zoey to fill shape in the color green
zoey.begin_fill() # zoey begins to fill shape
right_side_of_tree() # call on function right_side_of_tree
zoey.end_fill() # zoey stops filling shape

zoey.pu() # lift pen up
zoey.goto(-360,-238) # move zoey to -360,-238
zoey.width(10) # sets the line width that zoey will draw equal to 10
zoey.color("green") # set zoey's color to green
zoey.fillcolor("green") # tell zoey to fill shape in the color green
zoey.begin_fill() # zoey begins to fill shape
left_side_of_tree() # call on function left_side_of_tree
zoey.end_fill() # zoey stops filling shape
zoey.width(2) # sets the line width that zoey will draw equal to 2

# Drawing the triangle tree located on the right side of the house
zoey.pu() # lift pen up
zoey.goto(309,-238) # move zoey to 309,-238
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.rt(155) # rotate zoey to the right by 155 degrees
tree_trunk() # call on function tree_trunk

zoey.pu() # lift pen up
zoey.goto(279,-238) # move zoey to 279,-238
zoey.width(10) # sets the line width that zoey will draw equal to 10
zoey.color("green") # set zoey's color to green
zoey.fillcolor("green") # tell zoey to fill shape in the color green
zoey.begin_fill() # zoey begins to fill shape
right_side_of_tree() # call on function right_side_of_tree
zoey.end_fill() # zoey stops filling shape

zoey.pu() # lift pen up
zoey.goto(279,-238) # move zoey to 279,-238
zoey.width(10) # sets the line width that zoey will draw equal to 10
zoey.color("green") # set zoey's color to green
zoey.fillcolor("green") # tell zoey to fill shape in the color green
zoey.begin_fill() # zoey begins to fill shape
left_side_of_tree() # call on function left_side_of_tree
zoey.end_fill() # zoey stops filling shape
zoey.width(2) # sets the line width that zoey will draw equal to 2

# Drawing The Chimeney
zoey.pu() # lift pen up
zoey.goto(102,103) # move zoey to 102,103
zoey.color("brown") # set zoey's color to brown
zoey.fillcolor("brown") # tell zoey to fill shape in the color brown
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.lt(25) # rotate zoey to the left by 25 degrees
zoey.fd(70) # move zoey forward 70
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(50) # move zoey forward 50
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.fd(118) # move zoey forward 118
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Bricks
zoey.pu() # lift pen up
zoey.goto(-182,-262) # move zoey to -182,-262
zoey.color("red") # set zoey's color to red
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.fd(138) # move zoey forward 138
zoey.ht() # hide zoey

zoey.pu() # lift pen up
zoey.goto(45,-262) # move zoey to 45,-262
bricks1() # call on function bricks1

zoey.pu() # lift pen up
zoey.goto(-182,-235) # move zoey to -182,-235
bricks1() # call on function bricks1

zoey.pu() # lift pen up
zoey.goto(45,-235) # move zoey to 45,-235
bricks1() # call on function bricks1

zoey.pu() # lift pen up
zoey.goto(-182,-208) # move zoey to -182,-208
bricks1() # call on function bricks1

zoey.pu() # lift pen up
zoey.goto(45,-208) # move zoey to 45,-208
bricks1() # call on function bricks1

zoey.pu() # lift pen up
zoey.goto(-182,-181) # move zoey to -182,-181
bricks2() # call on function bricks2

zoey.pu() # lift pen up
zoey.goto(-63,-181) # move zoey to -63,-181
bricks3() # call on function bricks3

zoey.pu() # lift pen up
zoey.goto(45,-181) # move zoey to 45,-181
bricks3() # call on function bricks3

zoey.pu() # lift pen up
zoey.goto(157,-181) # move zoey to 157,-181
bricks2() # call on function bricks2

zoey.pu() # lift pen up
zoey.goto(-182,-154) # move zoey to -182,-154
bricks2() # call on function bricks2

zoey.pu() # lift pen up
zoey.goto(-63,-154) # move zoey to -63,-154
bricks3() # call on function bricks3

zoey.pu() # lift pen up
zoey.goto(45,-154) # move zoey to 45,-154
bricks3() # call on function bricks3

zoey.pu() # lift pen up
zoey.goto(157,-154) # move zoey to 157,-154
bricks2() # call on function bricks2

zoey.pu() # lift pen up
zoey.goto(-182,-127) # move zoey to -182,-127
bricks2() # call on function bricks2

zoey.pu() # lift pen up
zoey.goto(-63,-127) # move zoey to -63,-127
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.fd(125) # move zoey forward 125
zoey.ht() # hide zoey

zoey.pu() # lift pen up
zoey.goto(155,-127) # move zoey to 155,-127
bricks2() # call on function bricks 2

zoey.pu() # lift pen up
zoey.goto(-182,-100) # move zoey to -182,-100
bricks5() # call on function bricks5

zoey.pu() # lift pen up
zoey.goto(-182,-73) # move zoey to -182,-73
bricks4() # call on function bricks4

zoey.pu() # lift pen up
zoey.goto(154,-73) # move zoey to 154,-73
bricks4() # call on function bricks4

zoey.pu() # lift pen up
zoey.goto(-182,-46) # move zoey to -182,-46
bricks6() # call on function bricks6

zoey.pu() # lift pen up
zoey.goto(123,-46) # move zoey to 123,-46
bricks6() # call on function bricks6

zoey.pu() # lift pen up
zoey.goto(-182,-19) # move zoey to -182,-19
bricks5() # call on fucntion bricks5

zoey.pu() # lift pen up
zoey.goto(-157,8) # move zoey to -157,8
bricks7() # call on fucntion bricks7

zoey.pu() # lift pen up
zoey.goto(46,8) # move zoey to 46,8
bricks7() # call on fucntion bricks7

zoey.pu() # lift pen up
zoey.goto(-130,35) # move zoey to -130,35
bricks8() # call on function bricks8

zoey.pu() # lift pen up
zoey.goto(46,35) # move zoey to 46,35
bricks8() # call on function bricks8

zoey.pu() # lift pen up
zoey.goto(-104,62) # move zoey to -104,62
bricks9() # call on function bricks9

zoey.pu() # lift pen up
zoey.goto(46,62) # move zoey to 46,62
bricks9() # call on function bricks9

zoey.pu() # lift pen up
zoey.goto(-76,89) # move zoey to -76,89
bricks10() # call on function bricks 10

zoey.pu() # lift pen up
zoey.goto(46,89) # move zoey to 46,89
bricks10() # call on function bricks 10

zoey.pu() # lift pen up
zoey.goto(-48,116) # move zoey to -48,116
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.fd(100) # move zoey forward 100
zoey.ht() # hide zoey

zoey.pu() # lift pen up
zoey.goto(-21,143) # move zoey to -21,143
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.fd(45) # move zoey forward 45
zoey.ht() # hide zoey

zoey.pu() # lift pen up
zoey.rt(90) # rotate zoey to the right by 90 degrees
zoey.goto(0,143) # move zoey to 0,143
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-30,116) # move zoey to -30,116
divide_bricks2() # call on function divide_bricks2

zoey.pu() # lift pen up
zoey.goto(30,116) # move zoey to 30,116
divide_bricks2() # call on function divide_bricks2

zoey.pu() # lift pen up
zoey.goto(-61,35) # move zoey to -61,35
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-61,89) # move zoey to -61,89
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(61,89) # move zoey to 61,89
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-76,63) # move zoey to -76,63
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(76,63) # move zoey to 76,63
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-110,35) # move zoey to -110,35
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-61,35) # move zoey to -61,35
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(110,35) # move zoey to 110,35
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(61,35) # move zoey to 61,35
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-137,8) # move zoey to -137,8
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-85,8) # move zoey to -85,8
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-31,2) # move zoey to -31,2
divide_bricks3() # call on function divide_bricks3

zoey.pu() # lift pen up
zoey.goto(31,2) # move zoey to 31,2
divide_bricks3() # call on function divide_bricks3

zoey.pu() # lift pen up
zoey.goto(137,8) # move zoey to 137,8
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(85,8) # move zoey to 85,8
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-161,-18) # move zoey to -161,-18
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-119,-18) # move zoey to -119,-18
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(161,-18) # move zoey to 161,-18
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(119,-18) # move zoey to 119,-18
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-153,-46) # move zoey to -153,-46
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(153,-46) # move zoey to 153,-46
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-140,-86) # move zoey to -140,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(-104,-86) # move zoey to -104,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(-72,-86) # move zoey to -72,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(-50,-86) # move zoey to -50,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(-34,-86) # move zoey to -34,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(-9,-86) # move zoey to -9,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(140,-86) # move zoey to 140,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(104,-86) # move zoey to 104,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(72,-86) # move zoey to 72,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(50,-86) # move zoey to 50,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(34,-86) # move zoey to 34,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(9,-86) # move zoey to 9,-86
divide_bricks4() # call on function divide_bricks4

zoey.pu() # lift pen up
zoey.goto(-119,-18) # move zoey to -119,-18
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-143,-209) # move zoey to -143,-209
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-100,-209) # move zoey to -100,-209
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(143,-209) # move zoey to 143,-209
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(100,-209) # move zoey to 100,-209
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-122,-236) # move zoey to -122,-236
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-71,-236) # move zoey to -71,-236
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(122,-236) # move zoey to 122,-236
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(71,-236) # move zoey to 71,-236
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-160,-262) # move zoey to -160,-262
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(-100,-262) # move zoey to -100,-262
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(160,-262) # move zoey to 160,-262
divide_bricks() # call on function divide_bricks

zoey.pu() # lift pen up
zoey.goto(100,-262) # move zoey to 100,-262
divide_bricks() # call on function divide_bricks

# Drawing The Heart on The Door
zoey.pu() # lift pen up
zoey.goto(-15,-175) # move zoey to -20,-175
zoey.width(3) # sets the line width that zoey will draw equal to 3
zoey.lt(90) # rotate zoey to the left by 90 degrees
zoey.color("black") # set zoey's color to black
zoey.fillcolor("hot pink") # tell zoey to fill shape in the color hot pink
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.fd(10) # move zoey forward 10
zoey.rt(45) # rotate zoey to the right by 45 degrees
zoey.fd(10) # move zoey forward 10
zoey.lt(90) # rotate zoey to the left by 90 degrees
for i in range(4): # create a for loop that repeats the code four times
  zoey.fd(10) # move zoey forward 10
  zoey.rt(45) # rotate zoey to the right by 45 degrees
zoey.fd(34) # move zoey forward 34
zoey.rt(90) # rotate zoey to the right by 90 degrees 
zoey.fd(34) # move zoey forward 34
for i in range(2): # create a for loop that repeats the code twice
  zoey.rt(45) # rotate zoey to the right by 45 degrees
  zoey.fd(10) # move zoey forward 10
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey

# Drawing The Rainbow
zoey.pu() # lift pen up
zoey.goto(370,210) #move zoey to 370,210
zoey.width(6) # sets the line width that zoey will draw equal to 6
zoey.color("red") # set zoey's color to red
zoey.lt(75) # rotate zoey to the left by 75 degrees
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(120,120) # create a circle with a radius of 120,120
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.goto(365,207) #move zoey to 365,207
zoey.rt(119) # rotate zoey to the right by 119 degrees
zoey.color("orange") # set zoey's color to orange
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(115,115) # create a circle with a radius of 115,115
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.goto(360,204) #move zoey to 360,204
zoey.rt(114) # rotate zoey to the right by 114 degrees
zoey.color("yellow") # set zoey's color to yellow
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(110,110) # create a circle with a radius of 110,110
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.goto(355,201) #move zoey to 355,201
zoey.rt(109) # rotate zoey to the right by 109 degrees
zoey.color("green") # set zoey's color to green
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(105,105) # create a circle with a radius of 105,105
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.goto(350,198) #move zoey to 350,198
zoey.rt(104) # rotate zoey to the right by 104 degrees
zoey.color("blue") # set zoey's color to blue
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(100,100) # create a circle with a radius of 100,100
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.goto(345,195) #move zoey to 345,195
zoey.rt(99) # rotate zoey to the right by 99 degrees
zoey.color("purple") # set zoey's color to purple
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(95,95) # create a circle with a radius of 95,95
zoey.ht() # hide zoey

# Drawing The Sun
zoey.pu() # lift pen up
zoey.goto(-314,220) # move zoey to -314,220
zoey.color("gold") # set zoey's color to gold
zoey.fillcolor("gold") # tell zoey to fill shape in the color gold
zoey.begin_fill() # zoey begins to fill shape
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.circle(40) # print circle with a radius of 40
zoey.end_fill() # zoey stops filling shape
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.rt(130) # rotate zoey to the right by 130 degrees
zoey.goto(-290,235) # move zoey to -290,235
zoey.st() # show zoey
zoey.pd() # put pen down
zoey.fd(30) # move zoey forward 30
zoey.ht() # hide zoey
zoey.pu() # lift pen up
zoey.goto(-257,222) # move zoey to -257,222
sun_rays() # call on function sun_rays
zoey.pu() # lift pen up
zoey.goto(-243,192) # move zoey to -243,192
sun_rays() # call on function sun_rays
zoey.pu() # lift pen up
zoey.goto(-257,160) # move zoey to -257,160
sun_rays() # call on function sun_rays
zoey.pu() # lift pen up
zoey.goto(-290,144) # move zoey to -290,144
sun_rays() # call on function sun_rays
zoey.pu() # lift pen up
zoey.goto(-320,160) # move zoey to -320,160
sun_rays() # call on function sun_rays
zoey.pu() # lift pen up
zoey.goto(-334,192) # move zoey to -334,192
sun_rays() # call on function sun_rays
zoey.pu() # lift pen up
zoey.goto(-320,222) # move zoey to -320,222
sun_rays() # call on function sun_rays

# Drawing The House Number
pen.pu() # lift pen up
pen.goto(-11,-200)  # move zoey to -11,-200
pen.color("white") # set pen color to white
pen.write("370", font = penstyle_house_number) # set font and write message

# Drawing Welcome Home Message
pen.pu() # lift pen up
pen.goto(-39,-125)  # move zoey to -39,-125
pen.color("black") # set text color to black
pen.write("Welcome", font = penstyle_welcome_sign) # set font and write message

pen.pu() # lift pen up
pen.goto(-23,-150) # move zoey to -23,-150
pen.write("Home", font = penstyle_welcome_sign) # set font and write message

time.sleep(4) # wait four seconds
zoey.clear() # remover everything zoey drew
pen.clear() # remove the writing
zoey.ht() # hide zoey
time.sleep(1) # wait one second
pen.goto(20,150) # move pen to 20,150
pen.write("Goodbye Little Turtles", font = penstyle_goodbye_message, align = "center") # print goodbye message and align it in the center of the screen