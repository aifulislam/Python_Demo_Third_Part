#Note: Here is not wrong function , but all function is not sported--
#04/11/2020-------

for i in range(5):
    print("Hello world")

for i in range(5):
    print(i)

for x in range(5):
    print("I love Bangladesh")

#Turtle----------
import turtle
turtle.shape("turtle")
turtle.speed(5)
for i in range(4):
    turtle.forward(200)
    turtle.left(90)

turtle.exitonclick()

#For loop--------
result = 0
for _ in range(50):
    result = result + 1

print("Result: ",result)

#For loop--------
result = 0
num = 1
for num in range(51):
    result = result + num
    #result += num

print("Result: ",result)

#For loop--------
result = 0
for num in range(1,51):
    result = result + num
    #result += num

print("Result: ",result)

#For loop--------
for i in range(2, 11, 2):
    print(i)

#For loop, find maximum number--------
numbers = [3,5,1,6,8,2]
max_n = numbers[0]
for n in numbers:
    if n > max_n:
        max_n = n

print("Maximum : ",max_n)

#For loop, find minimum number--------
numbers = [5,2,4,6,3]
min_n = numbers[0]
for n in numbers:
    if n < min_n:
        min_n = n

print("Minimum : ",min_n)

#For loop, find minimum number--------
numbers = [2,5,6,1,8,9]
min_n = numbers[0]
for n in numbers:
    if min_n > n:
        min_n = n

print("Minimum : ",min_n)

#even----------
result = 0
for num in range(51):
    if num % 5 == 0:
        print(num)
        result += num

print("Sum is : ",result)

#odd--------
result = 0
for num in range(5,51,5):
    print(num)
    result += num

print("Sum is : ",result)

#Even------
print("Even----------")
result = 0
for num in range(2,11,2):
    result += num
    print(num)

print("Sum all even : ",result)

#Odd------
print("Odd----------")
result = 0
for num in range(1,11,2):
    result += num
    print(num)

print("Sum all odd : ",result)

#turtle----------
import turtle
turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()

#turtle----------
import turtle
turtle.speed(3)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick()

#Loop into Loop--------
#Nested loop--------

import turtle
turtle.shape("turtle")
turtle.speed(2)

for side_length in range(50,100,10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()

#Loop whith loop---------
saarc = ["Bangladesh","Afganistan","Pakistan","India","Butan","Sri Lanka","Nepal"]
for country in saarc:
    print(country,"is a member of SAARC")

#Loop whith loop---------
student = ["Arif","Tamim","Nahid","Ayon","Nazim"]
for student in student:
    print(student,"is a student")

#range using list()-------
li = list(range(10))
print(li)

#range using list()-------
li = list(range(2,21,2))
print(li)

#while loop----------
i = 0
while i < 5:
    print(i)
    i += 1

#while loop----------
print("Even------")
i = 20
while i < 31:
    print(i)
    i += 2

#while loop----------
print("Odd------")
i = 21
while i < 30:
    print(i)
    i += 2

#while loop----------
i = 5
while i > 0:
    i -= 1
    print(i)

#Multipliction_table----------
n = input("Please enter a positive integer: ")
n = int(n)
m = 1
while m <= 10:
    print(n,"X", m,"=" , n*m)
    m+= 1

#Multipliction_table----------
n = input("Enter a number: ")
n = int(n)
m = 1
while m <= 10:
    print(n, "X", m, "=", n * m)
    m += 1

#turtle----------
import turtle
turtle.color("orange")
turtle.speed(2)
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
        turtle.right(10)
        counter += 1

turtle.exitonclick()

#turtle----------
import turtle
height = 5
width = 5
turtle.speed(2)
turtle.penup()
for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)

    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()

#break and continue-------
while True:
    n = input("Enter a number : ")
    n = int(n)
    if n == 0:
        break
    print("Square of",n, "is", n*n)

#break and continue-------
while True:
    n = input("Please enter a positive number: ")
    n = int(n)
    if n < 0:
        print("We only allow positive number. Please try again. ")
        continue
    if n == 0:
        break
    print("Square of", n, "is", n*n)

#break and continue-------
terminate = False
while not terminate:
    number1 = input("Please enter a number: ")
    number1 = int(number1)
    number2 = input("Please enter another number: ")
    number2 = int(number2)
    while True:
        operation = input("Please enter add/sub or quit exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not  in ["odd", "sub"]:
            print("Unknown operation!")
            continue
        if operation == "odd":
            print("Result is", number1 + number1)
            break
        if operation == "sub":
            print("Result is", number1 - number1)
            break

