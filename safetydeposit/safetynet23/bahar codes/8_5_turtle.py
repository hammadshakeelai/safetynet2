import turtle
turtle.circle(100)

######################
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
######################
turtle.pensize(5)
turtle.pencolor('red')
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.setup(840, 680)

screen = turtle.Screen()
screen.bgcolor('lightblue')
#turtle.reset()
#turtle.clear()
#turtle.clearscreen()
turtle.done() 