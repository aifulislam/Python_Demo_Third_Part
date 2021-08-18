#20/12/2020
#Tamim Shahriar subeen----
#Lesson10--------
#Random--------
#Find of Number--------

import random

number = random.randint(1, 1000)
attempts = 0
while True:
    input_number = input("Guess the number (between 1 and 1000): ")
    input_number = int(input_number)
    attempts += 1
    if input_number == number:
        print("Yes, your guess is correct!")
        break
    if input_number > number:
        print("Incorrect! Please try to guess a smaller number.")
    else:
        print("Incorrect! Please try to guess a larger number.")

print("You tried", attempts, "times to find the correct number.")


p = 5/2
print(p)

p = 5//2
print(p)

p = 10/3
print(p)

p = 5//3
print(p)


import random
number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000

while True:
    print("Guess the number (between 1 and 1000): ")
    input_number = (low + high) // 2
    attempts += 1
    if input_number == number:
        print("Yes, your guess number is correct!")
        break
    if input_number > number:
        print("Incorrect! Please try to guess a smaller number.")
        high = input_number - 1
    else:
        print("Incorrect! Please try to guess a larger number.")
        low = input_number + 1

print("You tried", attempts, "times to find the correct number.")

