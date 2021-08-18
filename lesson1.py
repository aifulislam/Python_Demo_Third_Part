#01/11/2020
#Tamim Shahriar subeen----
#Lesson1--------

print("Hello World")

number1 = 10
number2 = 5
result = number1 + number2
print(result)

number11 = 50
print(number11)

my_money = 30
rickshaw_fare = 40
hh = my_money >= rickshaw_fare
print(hh)

my_money = 30
rickshaw_fare = 40
hh = my_money <= rickshaw_fare
print(hh)

print("Today")
p = "today" == "Tue"
print(p)
d = "tue" == "tue"
print(d)

today = "tue"
u = not (today == "tue")
print(u)

num = 20
a = num < 10
print(a)

b = num > 10
print(b)

c = num < 100
print(b)

d = num > 10 and num < 100
print(d)

e = num > 10 or num < 100
print(d)

f = not(num < 100)
print(f)

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[8])

number1 = input("Please inter number1: ")
number2 = input("Please inter number2: ")
number1 = int(number1)
number2 = int(number2)
print("number1+number2 = ",number1+number2)

#if statment--------
saarc = ["Bangladesh","Afganistan","Pakistan","India","Butan","Sri Lanka","Nepal"]
print(saarc)
print(saarc[2])
print(saarc[4])
tr = "Bangladesh" in saarc
print(tr)
tr = "China" in saarc
print(tr)
tr = "Bangladesh" not in saarc
print(tr)

#if statment--------
saarc = ["Bangladesh","Afganistan","Pakistan","India","Butan","Sri Lanka","Nepal"]

country = input("Enter the name of country: ")
if country in saarc:
    print(country,"is a member of SAARC")
print("Program terminated")

#if ,else statment--------
studentlist = ["Arif","Tamim","Nazim","Fahim","Ayon","Nahid"]
student = input("Enter tha name of student: ")
if student in studentlist:
    print(student,"is a student")
else:
    print(student,"is not a student")
print("Program End")

#if else statment--------
marks = input("Enter your marks: ")
marks = int(marks)
if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
elif marks >= 33:
    grade = "D"
else:
    grade = "F"

print("Your grade is: ",grade)

