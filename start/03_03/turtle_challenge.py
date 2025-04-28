"""
Chapter 3 challenge.
The world is your Turtle! 
"""
import turtle
import random

# --- Setup screen ---
screen = turtle.Screen()
screen.title("CYBER RACE 2077")
screen.bgcolor("#0d0221")  # Dark cyberpunk background
screen.setup(width=800, height=600)

# --- Create chequered flag ---
flag = turtle.Turtle(visible=False)
flag.shape("square")
flag.shapesize(stretch_wid=1, stretch_len=1)
flag.speed(0)
flag.penup()
flag.goto(350, 250)
flag.pendown()
flag.setheading(270)

colors = ["#00f0ff", "#ff00f0"]  # Neon blue and neon pink
for i in range(25):
    flag.color(colors[i % 2])
    flag.stamp()
    flag.forward(20)

# --- Create racers ---


def create_racer(color, y_pos):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.shapesize(2)
    racer.pensize(3)
    racer.speed(0)
    racer.penup()
    racer.goto(-350, y_pos)
    return racer


racer1 = create_racer("#00ffea", -100)  # Neon Cyan
racer2 = create_racer("#ff007f", 100)   # Neon Pink

# Spin for effect
for racer in (racer1, racer2):
    for _ in range(36):
        racer.right(10)

# --- Race! ---

# Draw starting line
start_line = turtle.Turtle(visible=False)
start_line.color("#fffa65")
start_line.pensize(5)
start_line.penup()
start_line.goto(-350, 300)
start_line.right(90)
start_line.pendown()
start_line.forward(600)

while racer1.xcor() < 350 and racer2.xcor() < 350:
    racer1.forward(random.randint(5, 15))
    racer2.forward(random.randint(5, 15))

# --- End ---
turtle.done()
