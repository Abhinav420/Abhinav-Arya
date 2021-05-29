import turtle
import random

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.bgcolor('black')
ssize = [10,15,20,25,30,35,40,45,50]
scolors = ["red","yellow","orange","green","blue","white"]

t = turtle.Turtle()
t.color("white")

stars = turtle.Turtle()
stars.color('white')

text = turtle.Turtle()

#Moon Funtion for draw the moon
def moon():
    t.penup()
    t.goto(-500,300)
    t.pendown() 
    t.right(140)
    t.speed(0)
    t.begin_fill()
    for i in range(210):
        t.forward(2)
        t.left(1)
    t.left(147)
    for i in range(150):
        t.forward(2)
        t.right(1)
    t.fillcolor("white")
    t.end_fill()

#star function for draw stars
def star(pos,color):
    color = color
    x,y = pos
    stars.speed(10)
    stars.color(color)
    stars.penup()
    stars.goto(x,y)
    stars.pendown()
    stars.begin_fill()
    for i in range(5):
        stars.forward(60)
        stars.left(144)
    stars.fillcolor(color)
    stars.end_fill()

#Text Function 
def write_txt(color):
    text.color(color)
    text.penup()
    text.goto(-180,-270)
    text.pendown()
    text.speed(5)
    style = ("stencil std Bold", 50, "normal")
    #Write Your msg = enter your msg below
    text.write("Good Night", font=style, move=True)

#Random funtions 
def rand_pos():
    return(random.randint(-640,640), random.randint(-350,350))
def rand_len():
    return(random.randint(10,50))

moon()
for i in range(20):
    color = random.choice(scolors)
    pos = rand_pos()
    length = random.choice(ssize)
    star(pos,color)
    write_txt(color)
    
turtle.done()