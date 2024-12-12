import turtle
#turtle.hideturtle()
#turtle.showturtle()
turtle.goto(0, 100) # Change the direction
turtle.write(turtle.pos())
#turtle.write("Turtle reached (0, 100)")
turtle.goto(-100, 0)
turtle.write(turtle.pos())

# 0 (No animation jump direct). 1 (Slowest), 10 (Fastest)
turtle.speed(1) # Default 6 (Moderate)
turtle.goto(0, 0)
#turtle.write("Turtle Stoped")
turtle.write(turtle.pos())
print(turtle.xcor())
print(turtle.ycor())

turtle.done() 