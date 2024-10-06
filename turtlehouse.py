import turtle
turtle.speed(10)
turtle.penup()
turtle.left(90)
turtle.hideturtle()
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.pendown()
turtle.forward(180)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(100)
turtle.left(30)
turtle.forward(60)
turtle.left(120)
turtle.forward(60)
turtle.left(120)
turtle.forward(60)
turtle.penup()
turtle.forward(180)
turtle.left(120)
turtle.pendown()
turtle.forward(60)
turtle.left(60)
turtle.forward(180)
turtle.left(60)
turtle.forward(60)
turtle.left(30)
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
turtle.backward(10)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.forward(5)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(30)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.forward(90)
turtle.backward(90)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(90)
turtle.penup()
turtle.goto(200,200)
turtle.setheading(180)
turtle.forward(30)
turtle.setheading(90)
turtle.forward(15)
turtle.pendown()
turtle.setheading(0)
turtle.circle(10)



import turtle

# Set up the window
window = turtle.Screen()
window.title("Turtle Car Drawing")
window.bgcolor("lightblue")

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.speed(4)  # Set the turtle's drawing speed

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw a circle (used for wheels)
def draw_circle(color, radius):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Start drawing the car body
pen.penup()
pen.goto(-100, 0)  # Move the turtle to the starting position
pen.pendown()

# Draw the main body of the car (rectangle)
draw_rectangle("blue", 200, 50)

# Move to the position to draw the top of the car
pen.penup()
pen.goto(-60, 50)
pen.pendown()

# Draw the car roof (smaller rectangle)
draw_rectangle("blue", 120, 40)

# Draw the first wheel
pen.penup()
pen.goto(-70, -20)
pen.pendown()
draw_circle("black", 20)

# Draw the second wheel
pen.penup()
pen.goto(50, -20)
pen.pendown()
draw_circle("black", 20)

# Hide the turtle (pen) after drawing is complete
pen.hideturtle()

# Close the window on click
window.exitonclick()



turtle.speed(1)
turtle.penup()
turtle.circle(56)
turtle.circle(56)
turtle.circle(56)
turtle.circle(56)
turtle.circle(56)
turtle.done