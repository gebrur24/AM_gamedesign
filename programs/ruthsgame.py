#Ruth Gebru
#we are going to learn abt lists, funtions to list
#we are going to learn abt for loop
    #Start
    #input instruction
    #input list of words(animals)
    #import os and random
    #get loop
    #get borders
    #print instruction
    #get list of animals
    #get randomizer to select a random animal from the list 
    #import use input to guess a animal
    #print "you got it right" if the guess was correct
    #input break if the guess was correct
    #print "you got the wrong animal"if the guess was wrong
    #input "do you want to play again type yes or no"
    #input break if the user wants to stop playing"
    #end
import random
import os
os.system ('cls')
title="guessing game"
print('this is a guessing game and you will only get 5 tries and i hope you have fun')
list=['tiger','lion','elephant','cow','panda','monkey','dolphin','meerkat','snake', 'hyena']
random_animal=random.choice(list)
print(random_animal)
guess= input('guess what safari animal ')


if guess.lower() == random_animal.lower():
    print('yay!!!guess is correct')
else:
    print('awww!!guess is not correct')


