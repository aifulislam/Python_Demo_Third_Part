#20/11/2020
#Tamim Shahriar subeen----
#Lesson09--------
#Data Structure-----(List[],Tuple(),Set{},dictionary{})
#List []----------
saarc = ["Bangladesh", "Pakistan", "India", "Sri Lanka", "Nepal", "Bhutan"]
print(saarc)
print(type(saarc))

#List using append()---
print("using append()---")
saarc = ["Bangladesh", "Pakistan", "India", "Sri Lanka", "Nepal", "Bhutan"]
saarc.append("Afganistan")
print(saarc)

#List using sort()---
print("using sort()---")
saarc = ["Bangladesh","Pakistan","India","Sri Lanka","Nepal","Bhutan"]
saarc.sort()
print(saarc)

#List using reverse()---
print("using reverse()---")
saarc = ["Bangladesh","Pakistan","India","Sri Lanka","Nepal","Bhutan"]
saarc.reverse()
print(saarc)

#List using insert()---
print("using insert()---")
fruits = ["Mango", "Banana", "Orange"]
fruits.insert(0, "Apple")
print(fruits)

#List using remove()---
print("using remove()---")
fruits = ["Mango", "Banana", "Orange", "Apple"]
fruits.remove("Banana")
print(fruits)

#List using remove() with condition---
print("using remove() with condition---")
fruits = ["Mango", "Banana", "Orange", "Apple"]
item = ("pineapple")
if item in fruits:
    fruits.remove(item)
else:
    print(item, "not in list")

#List using pop()---
print("using pop()---")
fruits = ["Mango", "Banana", "Orange", "Apple"]
fruits.pop()
print(fruits)

#List using extend()---
print("using extend()---")
li = [1,2,3,4]
li2 = [5,6,7,8]
li.extend(li2)
print(li)

#List using count()---
print("using count()---")
li = [1, 2, 3, 4, 5, 3, 6]
li.count(3)
print(li)

#List using del()---
print("using del()---")
li = [1, 2, 3, 4, 5, 6]
del(li[4])
print(li)

#List using append()---
print("using append()---")
li = []
for x in range(11):
    li.append(x)

print(li)

#List using add()---
print("using add()---")
li1 = [1,2,3,4,5]
li2 = [6,7,8,9,10]
li = li1 + li2
print(li)

#List using multi()---
print("using multi()---")
li1 = [1,2,3]
li2 = [6,7,8]
li = li1 * 3
print(li)

#List using multi()---
print("using multi()---")
li1 = ["a", "b", "c"]
print(li1)
str = "".join(li1)
print(str)

li2 = ["a", "r", "i", "f"]
print(li2)
str2 = "".join(li2)
print(str2)

li2 = ["a", "r", "i", "f"]
print(li2)
str2 = ",".join(li2)
print(str2)

li2 = ["a", "r", "i", "f"]
print(li2)
str2 = " - ".join(li2)
print(str2)

li2 = ["a", "r", "i", "f"]
print(li2)
str2 = " + ".join(li2)
print(str2)

#List comprehensions---------
print("List comprehensions---------")
li = [1, 2, 3, 4]
new_li = []
for x in li:
    new_li.append(2 * x)

print(li)
print(new_li)

#List comprehensions---------
print("List comprehensions---------")
li2 = [2, 4, 6, 8]
new_li2 = []
for i in li2:
    new_li2.append(3 * i)

print(li2)
print(new_li2)

#List comprehensions---------
print("List comprehensions---------")
li3 = [1, 2, 3, 4]
new_li3 = [2 * i for i in li3]
print(li3)
print(new_li3)

#List comprehensions---------
print("List comprehensions---------")
li4 = [7, 8, 9]
new_li4 = [3 * i for i in li4]
print(li4)
print(new_li4)

#List comprehensions---------
print("List comprehensions even numbers---------")
li5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for x in li5:
    if x % 2 == 0:
        even_numbers.append(x)

print(li5)
print(even_numbers)

#List comprehensions---------
print("List comprehensions even numbers---------")
li5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(li5)
print(even_numbers)

#List comprehensions---------
print("List comprehensions odd numbers---------")
li6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for i in li6:
    if i % 2 != 0:
        odd_numbers.append(i)

print(li6)
print(odd_numbers)

#List comprehensions---------
print("List comprehensions odd numbers---------")
li6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(li6)
print(odd_numbers)

#List comprehensions---------
print("List comprehensions odd numbers---------")
li6 = [1, 2, 3, 4]
odd_numbers = [x * x for x in range(1, 5)]
print(li6)
print(odd_numbers)

#Tuple------------
#x = 1, 2, 3    #acceptable too---
x = (1, 2, 3)
print(x)
print(type(x))

x = 1
print(type(x))

x = 1,
print(type(x))

x = ()
print(type(x))

tp1 = (1, 2, 3)
x = tp1[2]
print(x)

#tuple is not mutable--
#using pack and unpack-----
numbers = (10, 20, 30, 40)
n1, n2, n3, n4 = numbers
print(numbers)
print(n1)
print(n4)

t = n1, n3
print(t)
print(type(t))

item = (1, 2, 3.2, ["a", "b", "c"], "apple", "mango")
for item in item:
    print(item, type(item))

print(item[2])

tp2 = (1, 2, 3)
li = list(tp1)
print(li)

#Set--------------
A = set()
print(A)
print(type(A))

item = {"pen", "laptop", "phone"}
print(item)
print(type(item))

li = [1, 2, 3, 4]
tpl = (1, 2, 3)
A = set(li)
print(A)
print(type(li))
print(tpl)
print(type(tpl))

b = set("Bangladesh")
print(b)
print(type(b))

c = set("Canada")
print(c)
print(type(c))

d = {1, 2, 3}
k = 1 in d
print(k)

A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}

C = A & B
print(C)

C = A | B
print(C)

C = A ^ B
print(C)

C = A - B
print(C)

C = B - A
print(C)

