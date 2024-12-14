import os
empId = 123
print("Emp ID accepted:",int(empId))
print("Input type:",type(empId))
print(empId + 888)
print("Name","Sachin","Jadhav")

#for num in range(0,5):
#    n = input()
#    list.append(float(n))

#print(list)

#file = open("./ConvertCSV.py","r")

#filewrite = open("./Text.py","w")

#i = 0
#for line in file:
#    if i ==5:
#        i += 1
#        continue
#    filewrite.write(line)
#    i += 1
#    print("Line",i)


#ip1,ip2,ip3,ip4 = input().split(" ")


#print(ip1,ip2,ip3,ip4)

str1 = 1000
str2 = 3
str3 = 450
stmt = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."

print(stmt.format(str1,str2,float(str3)))


if os.stat("./test.txt").st_size == 0: 
    print("File is empty")

lineCount = 0
with open("./test.txt","r") as fp:
    for line in fp:
        lineCount += 1
        if lineCount == 4:
            print("Line 4:",line)
            break


for i in range(1,6,1):
    for j in range(i):
        print(j+1, end = " ")
    print("\n")


#print(sum(range(1, int(input())+1)))

# multiplication table

ip = 4

for i in range(1,11,1):
    print(i * int(ip))


print("\n\n")
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num >  500 :
        break;
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

numtoCount = 23434324

count  = 0;
while(numtoCount > 0):
    numtoCount = numtoCount // 10
    count +=1
    
print("Number Count:",count)

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print("\n")


mylist = [ 3, 6, 10, 33, 66, 2]

for i in range(len(mylist),0, -1):
    print(mylist[i-1], end= ' ')

print("\n")
# print from -10 to -1

for i in range(-10, 0, 1):
    print(i)
else:
    print("Done!")

#Find Prime Numbers

start = 25
end = 50
i = 2
print("Prime Numbers between",start,"and",end)
for num in range(start, end+1, 1):
    for i in range(2,int(num/2),1):
        if num % i == 0:
            break
    else:
        print(num)

print("Fibonaci Series:\n")
fibNumMap = {}
def fibonacci(num):
    if(num <=1):
        return 1
    if fibNumMap.get(num) != None:
        return fibNumMap.get(num)

    fibNum = fibonacci(num - 1) + fibonacci(num - 2)
    print(fibNum)
    fibNumMap[num] = fibNum
    return fibNum


fibonacci(10)


print("Find Factorial of a number\n")

def factorial(num):
    if(num == 1):
        return 1
    return num * factorial(num-1)


#print(factorial(int(input("Enter a Number to find Factorial:"))))

print("reverse a number\n")


n = 76542 #int(input("Enter a number to reverse:"))
multiplyer = 1
newnumber = 0
while n != 0:
    remainder = n % 10
    newnumber = ( newnumber * 10) + remainder
    n = int(n /10)
    print("New Number:",newnumber , "Old Number:",n)


print("Reversed Number : ",newnumber)

print("Print old index Elements:")

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if(i % 2 !=0):
        print(my_list[i])


inputNum = input("Find cube of all number till:")

for i in range(1,int(inputNum)+1,1):
    print(i * i * i,"\n")


for i in range(5):
    for j in range(i+1):
        print("*",end=' ')
    print("\n")

for i in range(4,0,-1):
    for j in range(i):
        print("*",end=' ')
    print("\n")



print("Variable length Args::")
def method1(*args):
    for i in args:
        print(i)

method1(1,3,5,6,8)


def addSub(a,b):
    return (a+b), (a-b)

add, sub = addSub(19,14)

print("Addition:",add, "Substration:",sub)


def outerFun(a, b):
    def inner():
        return a+b
    return inner() + 5

print("Outer-Inner function:",outerFun(13,15))

def recAddition(a):
    if a == 0:
        return 0
    return a + recAddition(a-1)

print("Recursive Addition:", recAddition(10))

def display_student(name,age):
    print("Name:",name,"Age:",age)

show_tudent = display_student

show_tudent("Sachin", 30)


even_num_list = []

def even_num(start, end):

    for i in range(start,end,1):
        if i % 2 == 0:
            even_num_list.append(i)

even_num(4,31)
print(even_num_list)

x = [4, 6, 8, 24, 12, 2]
print("Max Number from List:", x)
print("Max Num:",max(x))

str = "MachineLearning"
print(str[0:1],  str[len(str)-1:len(str)], str[int(len(str)/2):int(len(str)/2)+1])


print(str[int(len(str)/2)-1:int(len(str)/2)+2])


print("New String")

str1 = "Amachine"
str2 = "Learning"

print(str1[0:int(len(str1)/2)] + str2 + (str1[int(len(str1)/2):]))


newString = str1[0]+str2[0]
newString += str1[int(len(str1)/2)]+str2[int(len(str2)/2)]+str1[len(str1)-1]+str2[len(str2)-1]

print("New String:",newString)

s1 = "PyThOn"

allLower =""
allUpper = ""
for c in s1:
    if c.islower():
        allLower += c
    else:
        allUpper += c

print("LowerToUpdateOder:",allLower+allUpper)


mixString  = "P@#yn26at^&i5ve"
charCount = 0
digitCount = 0
specialCharCount = 0

for ch in mixString:
    if ch.isalpha():
        charCount += 1
    elif ch.isdigit():
        digitCount += 1
    else:
        specialCharCount += 1


print("Char Count:",charCount,"Digit Count:",digitCount,"Special Char Count:",specialCharCount)


s1 = "Abc"
s2 = "Xyz"



def mergeStrigs(long,short):
    s3 = ""
    for index in range(len(short)):
        s3 += long[index]+short[index]
    return s3

print("Merged String:",mergeStrigs(s1,s2))


s1 = "Ax"
s2 = "PYAthon"

def checkChar(S1,S2):
    flag = True
    for char in S1:
        if char in S2:
            continue
        else:
            flag = False
    return flag

print("Is Char Exits:",checkChar(s1,s2))


str = "USA is a country, usa visa is difficult to get"

temp_str = str.lower()

print("Occurences::",temp_str.count("usa"))


mixStr = "PYnative29@#8496"

digitCount = 0
sum = 0;

for ch in mixStr:
    if ch.isdigit():
        digitCount += 1
        sum += int(ch)
print("sum :",sum, ", Average :",sum/digitCount)



new_str = "AppleBMCa"
map = {}
for c in new_str:
    count = new_str.count(c)
    map[c] = count

print(map)

print("reverse:",new_str[::-1])


longStr = "this is pune and BMC has a office in pune. Winter in india"

print("Long Index::",longStr.rfind("pune"))




str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print(list(filter( None,str_list)))


str_special = "/* this is BMC @developers & QA works here"

import string
print(string.punctuation)
print("Translate:",str_special.translate(str.maketrans('','',string.punctuation)))


for c in string.punctuation:
    str_special = str_special.replace(c,"#")
print("replace with # ::", str_special)


l1 = [3,6,9,12,15,18]
l2 = [2,4,6,8,10,12]

l3 = list()

l3 = l1[1::2] + l2[0::2]
print("L3 list:",l3)


list1 = [22,25,90,44,67,33]

list1.pop(4)

print(list1)

list1.insert(2,11)
list1.append(11)

print(list1)


new_sample_list = [11,54,33,56,77,22,00,44,55,61]
split_point = len(new_sample_list) / 3
print("Reverse 1",list(reversed(new_sample_list[:int(split_point)])))
print("Reverse 2",list(reversed(new_sample_list[int(split_point):int(split_point)*2])))
print("Reverse 3",list(reversed(new_sample_list[int(split_point)*2:len(new_sample_list)])))

# count elements

list1 = [10,21,22,33,44,31,21,6,3,49,80,10,22,22,3]

map = {}

for item in list1 :
    map[item] = list1.count(item)

print("Element count", map)



list1 = [2,3,4,5,6,7,8]
list2 = [4,9,16,25,36,49,64]

result = zip(list1,list2)
print("Zip result", set(result))


m1 = {2:4, 3:9, 4:16}
m2 = {11:121, 13:169, 14:196}

print("Ma zip result", set(zip(m1,m2)))


set1 = {10, 22, 12, 24, 56,7,8,78}
set2 = {11, 12, 24, 5, 3,88, 8}

print("Common", set1.intersection(set2))
print("Set1 after removing commons",set1 - set1.intersection(set2))

