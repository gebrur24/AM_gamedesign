#Ruth Gebru
#This is a string practice using an array
import os
os. system ('cls')
 #Create a string made of the first, middle and last character
message = "James"
#want jms
print (message [0],end='')
print (message [2],end='' )
print (message [4])
#Write a program to create a new string made of the middle three characters of an input string.
message = "JhonDipPeta"
middle= int (len(message)/2)
print (middle)
#want Dip
print (message [4], end= '')
print (message [5], end= '')
print (message [6])
message="JaSonAy"
#want Son
str1="JaSonAy"
print(str1[int(len(str1)/2) - 1], end = "")
print(str1[int(len(str1)/2)], end = "")
print(str1[int(len(str1)/2) + 1])
#This is a string practice using appended a new string in the middle of a given string
s1= 'Ault'
s2= 'Kelly'
word= s1[0:int(len( s1)/2)] +s2 +s1[int(len( s1)/2):int(len ( s1))]
# Write a program to create a new strings3by appendings2in the middle ofs1.
# word = s1[0:2] + s2 + s1[2:]
print(word)
#Create a new string made of the first, middle, and last characters of each input string
s1= 'America'
s2= 'Japan'
word= s1[0]+s2[0]+s1[int(len(s1)/2)]+ s2[int(len(s1/2-1))]+s1[int(len(s1)-1)]+s2[int(len(s2)-1)]
print (word)
#Arrange string characters such that lowercase letters should come first
str1= 'PyNaTive'
#outcome should be yaivePNT
word= str1[1]+ str1[3]+str1[5:8]+str1[0]+str1[2]+str1[4]
print(word)