#19/12/2020
#Tamim Shahriar subeen----
#Lesson10--------
#Random--------

import random
rm = random.random()
print(rm)

import random
rm2 = random.randint(10, 100)
print(rm2)

import turtle
po = turtle.position()
print(po)

turtle.forward(100)
po = turtle.position()
print(po)

turtle.left(90)
po = turtle.position()
print(po)

turtle.forward(100)
po = turtle.position()
print(po)

turtle.backward(300)
po = turtle.position()
print(po)

print("Random Turtle: ")
import turtle
import random

for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    turtle.dot()

turtle.done()

print("Random Turtle: ")
import turtle
import random

turtle.penup()
for i in range(30):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    turtle.setposition(x, y)
    turtle.dot()

turtle.done()


print("Random Turtle: ")
import turtle
import random
# List of Colors
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

for i in range(50):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)

    # set a random position
    turtle.setposition(x, y)
    # set a random color
    i = random.randint(0, len(colors)-2)
    turtle.dot(colors[i])

turtle.done()

