import turtle

# Set up the turtle and screen
screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(0)

# Set up the maze walls
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.goto(-200, -200)
turtle.goto(200, -200)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.goto(-100, -100)
turtle.goto(100, -100)
turtle.goto(100, 100)
turtle.goto(-100, 100)

# Set up the end goal
turtle.penup()
turtle.goto(180, 180)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Move the turtle using arrow keys
def move_up():
    turtle.setheading(90)
    turtle.forward(20)

def move_down():
    turtle.setheading(270)
    turtle.forward(20)

def move_left():
    turtle.setheading(180)
    turtle.forward(20)

def move_right():
    turtle.setheading(0)
    turtle.forward(20)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Check if the turtle has reached the end goal
def check_win():
    if turtle.distance(180, 180) < 25:
        turtle.write("You win!", align="center", font=("Arial", 36, "bold"))

screen.listen()
screen.mainloop()
