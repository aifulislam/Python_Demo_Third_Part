#05/11/2020-------
#Function----------

def add(n1,n2):
    return n1 + n2

n = 10
m = 20

result = add(n,m)
print(result)

#Function----------
x = 30
y = 40
result = add(x,y)
print(result)

print(add(2.50,6.50))

#Function----------
def sub(s1,s2):
    return s1 - s2


x = 100
y = 50
sum = sub(x,y)
print(sum)

#Function----------
def mul(m1,m2):
    return m1 * m2

p = 10
q = 20
multiplaction = mul(p,q)
print(multiplaction)

#Function----------
def myfnc(x):
    print("inside myfnc", x)
    x = 10
    print("inside myfnc", x)

x = 20
print(x)
myfnc(x)

#Function----------
def myfnc(y):
    print("y = ",y)
    print("x = ",x)

x = 20
myfnc(x)
print("y = ",x)

# Function----------
def myfnc(y=10):
    print("y = ", y)


x = 20
myfnc(x)
myfnc()

#Function----------
def myfunc(x, y , z = 10):
    print("x = ",x, "y = ",y, "z = ",z)

myfunc(x = 1, y = 2, z = 5)
a = 5
b = 6
myfunc(x = a, y = b)
a = 1
b = 2
c = 3
myfunc(y = a, z = b, x = c)

#Function----------
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result+= number
    return result

result = add_numbers([5,10,20,30,40,50])
print("Sum of result = ",result)

sum = add_numbers([5,8,5,4,6,7])
print("Sum of result = ",sum)

#Function----------
def test_fnc(li):
    li[0] = 10

my_list = [1,2,3,4,5]
print("before function call [",my_list)
test_fnc(my_list)
print("After function call [",my_list)

#Function----------
list1 = [1,2,3,4,5]
list2 = list1
print(list1)
print(list2)
list2[0] = 100
print(list2)
print(list1)

