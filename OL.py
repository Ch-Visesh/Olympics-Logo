import turtle

# object tr for turtle
ring = turtle.Turtle()

# set thikness for each ring
ring.pensize(5)

ring.color("blue")
ring.penup()
ring.goto(-110, -25)
ring.pendown()
ring.circle(45)

ring.color("black")
ring.penup()
ring.goto(0, -25)
ring.pendown()
ring.circle(45)

ring.color("red")
ring.penup()
ring.goto(110, -25)
ring.pendown()
ring.circle(45)

ring.color("yellow")
ring.penup()
ring.goto(-55, -75)
ring.pendown()
ring.circle(45)

ring.color("green")
ring.penup()
ring.goto(55, -75)
ring.pendown()
ring.circle(45)
 
turtle.done()