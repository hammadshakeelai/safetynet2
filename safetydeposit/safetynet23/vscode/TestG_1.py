# Hit the Target Game 
import turtle
counter=0
while True:
    counter+=1
    SCREEN_WIDTH = 600     # Screen width
    SCREEN_HEIGHT = 600    # Screen height
    TARGET_LLEFT_X = 100   # Target's lower-left X
    TARGET_LLEFT_Y = 250   # Target's lower-left Y
    TARGET_WIDTH = 25      # Width of the target
    FORCE_FACTOR = 30      # Arbitrary force factor
    PROJECTILE_SPEED = 1   # Projectile's animation speed
    NORTH = 90            # Angle of north direction
    SOUTH = 270           # Angle of south direction
    EAST = 0              # Angle of east direction
    WEST = 180            # Angle of west direction
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)
    if counter>9:
        print('Hint: 69,9.5')
    angle = float(input("Enter the projectile's angle: "))
    force = float(input("Enter the launch force (1−10): "))
    distance = force * FORCE_FACTOR
    turtle.setheading(angle)
    turtle.forward(distance)
    if (turtle.xcor() >= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and turtle.ycor() >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
    else:
        print('You missed the target.')