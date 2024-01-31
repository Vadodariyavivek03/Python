import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_eyes():
    turtle.color("black")
    draw_circle("black", 10, -20, 50)
    draw_circle("black", 10, 20, 50)

def draw_mouth():
    turtle.penup()
    turtle.goto(-20, 20)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(20, 180)

def draw_happy_face():
    turtle.speed(2)
    turtle.hideturtle()
    
    turtle.color("yellow")
    draw_circle("yellow", 50, 0, 0)
    
    draw_eyes()
    draw_mouth()

    turtle.done()

# Call the function to draw the happy face
draw_happy_face()


print("Thank You.")