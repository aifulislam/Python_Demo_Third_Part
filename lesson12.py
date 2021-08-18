#20/12/2020
#Tamim Shahriar subeen----
#Lesson10--------
#Random--------
#Turtle-----------

import turtle
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break

turtle.end_fill()
turtle.done()

#Turtle-----------
import turtle
turtle.begin_fill()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.end_fill()

p = 1.1 - 0.9
print(p)

