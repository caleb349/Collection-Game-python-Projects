# !/usr/bin/en python3
# -*- coding: utf-8 -*-
"""
title: Exercise 3
Card shuffling and dealing

@desc: This is a Python program that allows users 
to guess words from a book title of their choosing. 

@created:  tuesday 2/12/2018 18:15:11 2019
@author:   Caleb obi
@course:   Introduction to programming
@univ:     Wayne state University
@assign:   Exercise 3
@pyVerrsion: 3.7x
""" 
import datetime
print("-"*60)
# output welcome Message
print("Welcome to Collection Game")
# Ask User for name 
User_input = input('First Player : What is your name : ')
print(User_input)
# prompt second player options
User_input1 = input('Second Player : What is your name : ')
print(User_input1)
# Describe games to the user
print('-'*60)
print('Welcome', User_input, 'and', User_input1, 'to collection games')
print("Python program that allows users to input basic demographic information (minimum of three pieces of demographic information) and then to create a collection of three items, with each item having at least two pieces of metadata attached to them. After this initial phase of the game, each user is allowed to try and guess an item from the other's collection. Each user can only have X guesses (you define X, e.g., you could allow a user guess a maximum of 10 times) before the game ends. You can alternate guessing or have one user guess all their guesses at one time")
print('-'*60)
# Ask User for Otions
Option1 = input('First Player : Do you want to procedd with this Game or Quit : ')
if Option1 == "Q":
    print("Ohh....okay Thank you so much for Playing this game!!!..", User_input)
if Option1 == 'P':
        print("Welcome to collection game", User_input)
print('-'*60)        
# Ask Second Player for options
Option1 = input('Second Player : Do you want to procedd with this Game or Quit : ')
if Option1 == "Q":
    print("Ohh....okay Thank you so much for Playing this game!!!..", User_input1)    
if Option1 == 'P':
    print("Welcome to collection game", User_input1)
print('-'*60)        
## print Game Score
print(User_input, 'score : 0')
print(User_input1, 'score : 0')
# Ask User for First player Demographic information
Question1 = input('Player one : First name : ')
Question2 = input('player one : Last name : ')
# Question3 = input('Player one : Age : ')
## Check for string Value
Question3 = input ("Player one : Age : ")
if (Question3.isdigit()):
    print("Age is a valid number")
else:
        print("Age is a string")
print('-'*60)
print('Player one Demographic information')
print('-'*60)
## output player 1 Demographic information
print('First name: ', Question1)
print('Last name : ', Question2)
print('Age : ', Question3)
print('-'*60)
# Ask for Second Player Demographic information
Question4 = input('Player Two : First name : ')
Question5 = input('player Two : Last name : ')
Question6 = input ("Player Two : Age : ")
if (Question6.isdigit()):
    print("Age is a valid number")
else:
        print("Age is a string")
print('-'*60)
print('Player Two Demographic information')
print('-'*60)
## output player two Demographic information
print('First name: ', Question4)
print('Last name : ', Question5)
print('Age : ', Question6)
print('-'*60)
print("\n")
## Ask player two to close their Eyes
print(Question4, 'Please close you eyes for ', Question1, 'to begin the game')
## Ask player one to input information.
InfoQuestion1 = input('Sports : ')
infoQuestion2 = input('Player :  ')
infoQuestion3 = input('Rank: ')
if (infoQuestion3.isdigit()):
    print("rank is valid")
else:
        print("not a valid rank")
## output player one collection
print('-'*60)
print(Question1, 'collection')
print('-'*60)
print('Sports : ', InfoQuestion1)
print('player : ', infoQuestion2)
print('Rank : ', infoQuestion3)
print('-'*60)
print('\n')
# Ask player one to close their eyes
print(Question1, 'Please close you eyes for ', Question4, 'to begin the game')
#Ask player one to input information.
InfoQuestion4 = input('Sports : ')
infoQuestion5 = input('Player :  ')
infoQuestion6 = input('Rank: ')
if (infoQuestion6.isdigit()):
    print("rank is valid")
else:
        print("not a valid rank")
# output player one collection
print('-'*60)
print(Question4, 'collection')
print('-'*60)
print('Sports : ', InfoQuestion1)
print('player : ', infoQuestion2)
print('Rank : ', infoQuestion3)
print('-'*60)
print('\n')
# Allow Each player to Equess 
print('-'*60)
print('its your turn to guess', Question1)
# sport
GuessQuestion1 = input("What type of Sport for  : ")
if GuessQuestion1 == InfoQuestion4:
    print("Correct + one point added", Question1)
else :
    print("Wrong choice, Enter what type of sport : ")
# player
GuessQuestion2 = input("What type of player for  : ")
if  GuessQuestion2 == infoQuestion5:
    print("Correct + one point added", Question1)
else :
    print("Wrong choice, Enter what type if player : ")  
# rank
GuessQuestion3 = input("What rank position for  : ")
if   GuessQuestion3 == infoQuestion6:
    print("Correct + one point added", Question1)
else :
    print("Wrong choice, Enter rank Position : ")
print('-'*60)    
print('-'*60)

# Allow player two to guess    
print('its your turn to guess', Question4)
# sport
GuessQuestion4 = input("What type of Sport for  : ")
if GuessQuestion4 == InfoQuestion1:
    print("Correct + one point added", Question4)
else :
    print("Wrong choice, Enter what type of sport : ")
# player
GuessQuestion5 = input("What type of player for  : ")
if  GuessQuestion5 == infoQuestion2:
    print("Correct + one point added", Question4)
else :
    print("Wrong choice, Enter what type if player : ")  
# rank
GuessQuestion3 = input("What rank position for  : ")
if   GuessQuestion5 == infoQuestion3:
    print("Correct + one point added", Question4)
else :
    print("Wrong choice, Enter rank Position : ")

print('-'*60)
print('\n')    

# Ask player one if he or she wants to continue or quit
FinalQuestion = input('Would you like to quit or continue, C = Continue and Q = Quit : ', Question1) 
if FinalQuestion == 'C':
    print("Nice, lets continue !!", Question1)  
else :
    print("cool")

if FinalQuestion == 'Q':
    print("Ohh okayy.... thanks for playing see you next time", Question1)  

 # Ask player two if he or shw wants to continue or Quit 
FinalQuestion1 = input('Would you like to quit or continue, C = Continue and Q = Quit : ', Question4) 
if FinalQuestion1 == 'C':
    print("Nice, lets continue !!", Question4)  
else :
    print("cool")

if FinalQuestion == 'Q':
    print("Ohh okayy.... thanks for playing see you next time", Question4)  


