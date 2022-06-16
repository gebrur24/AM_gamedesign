#Ruth Gebru
#calculate age
#get user year and current year
import os 
os.system('cls')
by=2005 #assign this valueas a number
#by = input('year you were born')
by = int(input('year you were born,'))
currentYear=2022 #alas number
age = currentYear-by
print('  your age is', age)
#selection
if age >17:
    print ('you are young')