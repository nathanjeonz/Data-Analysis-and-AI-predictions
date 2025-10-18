import turtle
import numpy as np

t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t.penup()
t2.penup()
t3.penup()

t.goto(-400,0)
t2.goto(-400,0)
t3.goto(-400,0)

t.pendown()
t2.pendown()
t3.pendown()

t.color('red')
t2.color('blue')
t3.color('green')

for x in range(360*3):
    y = 100 * np.sin(np.radians(x))
    y2 = 100 * np.cos(np.radians(x))
    
    y3 = 100 * np.tan(np.radians(x))
    if y3> 500 or y3<-500:
        continue
    

    t.goto(x-400,y)
    t2.goto(x-400,y2)
    t3.goto(x-400,y3)

turtle.done()