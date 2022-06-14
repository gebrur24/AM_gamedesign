#Ruth Gebru
#we are going to learn abt lists, funtions to list
#we are going to learn abt for loop
import random
import os
from tkinter import N
os.system ('cls')

thislist=["appple," "banana,""cherry","orange","Kiwi","melon","mango"]
#           0           1       2         3        4      5    6  
#                                                   -4     -5   -6
print(thislist[1]) #print from a specific index
print(thislist[-1])# print form the end
print(thislist[2:5])# pring from two value the first one is included in the set the seind is exluded
print(thislist[:3])#print up to a value but not inluding a value
print(thislist[2:])# prints exeruthing after a value inluding the orginal element
print(thislist[-4:-1])#range of negative indexes

if "apple" in thislist:
        print("yes the apple is in the list")

for num in range (10):
    print(num,end= " ")

print()

for element in thislist:# element= thislist(times run throught the loop)
    print(element,end= " ")
print()

thislist.append("pinapple") 
print(thislist[0:])

#for num in range(10):
#    thislist.append(input("input a food"))
#print(thislist[0:])

thislist.insert(1,"pinapple")# adding a element to a specific index insert(index, element you want to add)
print(thislist[0:])

for i in range(len(thislist)):
    print(thislist[i], end= " / ")
print()

list_num = [1, 2, 3, 4]
list_num.extend(thislist)
print(list_num)

list_num = [1, 2, 3, 4]
list_num.append(thislist)
print(list_num)
print(list_num[-1])# print the last element
print(list_num[-1][0])# print a element in an eleemtn if that element is in list [0, 1, 2, 3]

word= random.choice(thislist)
print(word)

guess = input("input a food\t")
if guess in word:
    print("congrats you guessed the food")