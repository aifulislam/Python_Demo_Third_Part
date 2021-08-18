#07/11/2020
#Tamim Shahriar subeen----
#Lesson8--------
#String---------

s = "hello"
p = len(s)
print(s)

#String---------
s = ""
q = len(s)
print(q)

#String---------
s = "Dimik's"
print(s)

#String---------
s = "Dimik\'s"
print(s)

#String---------
country = "Bangladesh"
t = len(country)
print(t)
print(country)
print(country[-3])
print(country[3:-2])

#String---------
for c in country:
    print(c)

#String---------
c = ["A","B","C","D"]
print(c)
print(c[2])
print(c[-3])

#String---------
country = "Bangladesh"
print(country[0])

#String---------
country = "Bangladesh"
print(country.find("Ban"))
print(country.find("des"))

#String---------
country = "North Korea"
new_country = country.replace("North" , "South")
print(new_country)

#String---------
country = "Bangla" + "desh" + "123"
print(country)

#String---------
x = "10" + "10"
print(x)

#String----using find()-----

country = "Bangladesh"
print(country.find("Ban"))
print(country.find("des"))

#String----using replace()-----
country = "North Korea"
new_country = country.replace("North","South")
print(new_country)
print(country)

#String----using replace()-----
text = "this is a text. this is another text. this is final tex."
new_text = text.replace("this", "This")
print(text)
print(new_text)

#String----using replace()-----
text1 = "hello"
text1 = text1.replace("hello","Hello")
print(text1)

#String----using strip()-----
text2 = "  I am Ariful Islam  "
new_text1 = text2.split()
print(text2)

#String----using lstrip()-----
text3 = "  I am Ariful Islam"
new_text2 = text3.split()
print(text2)

#String----using rstrip()-----
text4 = "I am Ariful Islam "
new_text3 = text4.split()
print(text2)

#String -----using uppercase()------
s1 = "Bangladesh"
s1.upper()
print(s1)

#String -----using lowercase()------
s2 = "BANGLADESH"
s2.lower()
print(s2)

#String -----using capitalize()-----
s3 = "Bangladesh"
s3.capitalize()
print(s3)

#String----using split()-----
str = "I am Ariful Islam."
word = str.split()
print(word)
for x in word:
    print(x)

#String----using startswith()-----
str1 = "Mr. Ariful Islam"
if str1.startswith("Mr."):
    print("Md.")

#String----using startswith()-----
str = "Bangladesh"
str.startswith("Ban")
print("BD")

#String----using endswith()-----
str1 = "Mr. Ariful Islam"
if str1.endswith("Islam"):
    print("Md. Ariful (Arif)")


#String----using count()-----
str = "a quick brown for jump over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))

#String----using count()-----
print("Count -----2")
str1 = "I am Ariful Islam. I am a student. My country is Bangladesh. I live in Jeshore."
for x in "abcdefghijklmnopqrstuvwxyz":
    print(x, str1.count(x))


#String----using endswith()-----
import turtle
name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam, how are you?")
else:
    name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)

turtle.exitonclick()

