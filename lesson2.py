#02/11/2020-------
#Maximum----------
n1 = 50
n2 = 60
n3 = 70
if n1 < n2:
    max_n = n1
else:
    max_n = n2
if n3 < max_n:
    max_n = n3

print("Maximum : ",max_n)

#Minimum--------
n1 = 50
n2 = 40
n3 = 30
if n1 < n2:
    max_n = n1
else:
    max_n = n2
if n3 < max_n:
    max_n = n3

print("Minimum : ",max_n)

#Leap Year-----------
year = 2024
if year % 400 == 0:
    print("Yes")
elif year % 100 == 0:
    print("No")
elif  year % 4 == 0:
    print("Yes")
else:
    print("NO")

#Leap Year-----------
if year % 100 != 0 and year % 4 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes")

else:
    print("No")

