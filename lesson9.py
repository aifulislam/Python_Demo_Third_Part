#20/11/2020
#19/12/2020
#Tamim Shahriar subeen----
#Lesson09--------
#Data Structure-----(List[],Tuple(),Set{},dictionary{})
#Dictionary--------

marks = [77, 76, 65, 78, 62, 64, 60, 77, 75, 79]
roll = input("Enter your roll number: ")
print("Your marks is", marks[int(roll)-1])

#Dictionary--------
marks = [[74, 73], [70, 75], [68, 72], [73, 73]]
result = marks[int(4)-1]
print(result)

#Dictionary--------
marks = [77, 76, 65, 78, 62, 64, 60, 77, 75, 79]
roll = input("Enter your roll number: ")
print("your marks is", marks[int(roll)-1])

#Dictionary--------
marks = [[74, 73], [70, 75], [68, 72], [73, 73]]
print(marks[0])
print(marks[3])

marks = {1: 77, 2: 76, 5: 62, 4: 78, 3: 65}
print(type(marks))
print(marks[3])
print("Marks of roll number 4 is", marks[4])

marks = {1005: 75, 1003: 72, 1002: 70, 1001: 75, 1004: 77}
print(marks[1003])

marks = {"DH2001": 75, "DH1777": 72, "KH2050": 70}
print(marks["DH2001"])

dt = {}
print(dt)

print(type(dt))
dt[1] = "One"
print(dt[1])

dt[2] = "Two"
print(dt[2])

print(dt)

dt = {"a": "A", "b": "B", "c": "C"}
print(dt)
print(dt["a"])
print(dt["b"])

dt = {"a": "A", "b": "B", "c": "C"}
dt[(1, 2, 3)] = "tuple"
print(dt)
print(type(dt))

s = {1, 2, 3, 4}
print(s)
print(type(s))

bd_divition_info = {}
bd_divition_info["Barishal"] = {"district": 6, "upazila": 39, "union": 333}
bd_divition_info["Chittagong"] = {"district": 11, "upazila": 97, "union": 336}
bd_divition_info["Dhaka"] = {"district": 13, "upazila": 93, "union": 1833}
bd_divition_info["Khulna"] = {"district": 10, "upazila": 59, "union": 270}
bd_divition_info["Mymensingh"] = {"district": 4, "upazila": 34, "union": 350}
bd_divition_info["Rajshahi"] = {"district": 8, "upazila": 70, "union": 558}
bd_divition_info["Rangpur"] = {"district": 8, "upazila": 58, "union": 536}
bd_divition_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}

print(bd_divition_info)

divitions = bd_divition_info.keys()
print(divitions)

print("Divitions :-----------")
for divition in divitions:
    print(divition, "Divition")

print("Upazila :-----------")
for divition in divitions:
    print(divition, "Upazila", bd_divition_info[divition]["upazila"])

for item in bd_divition_info:
    print(item)

print("\n")
print("Methood: 1")
for key in bd_divition_info:
    print(key)
    print(bd_divition_info[key])
print("\n")

print("Methood: 2")
for key, value in bd_divition_info.items():
    print(key)
    print(value)

