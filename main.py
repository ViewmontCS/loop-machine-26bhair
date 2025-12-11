import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

#######    Your code here    #######
#Using loops, you will create a simple text-based slot machine.
#1. Setting up variables

#Create an integer that holds the user's score. The user will use their score to pay for playing, so initialize it to an amount that lets them play a reasonable number of times (100 should be good).

#Create an integer that holds the cost of playing the game.

#Create an integer that holds the payout for when the user wins (the payout should be more than the play cost). If you want to have varied payouts based on how they win, have multiple variables for each payout amount, with appropriate variable names.

#2. Welcome Message

#Print a welcome message to the player. It can be simple.

#3. Paying for the game

#Using a while loop, allow the user to play the game. If the user has no score left, exit the while loop. Subtract the play cost from the score here (5 is a fine amount).

#4. Slot Roll

#Begin the slot roll by clearing the terminal using the provided clear() function. Generate a set of 9 random numbers from 0-9 to display. Print the numbers so layout is as follows:
#|1|2|3|
#|4|5|6|
#|7|8|9|
#________________________________________________________________________________________
#thought proccesses:
# use a randint variable and print the brackets with the variable. Randint being 0-9
#need list to check for win. no randint

#
R1 = []
R2 = []
R3 = []
import random



money = 1000
play_cost = 200
Payout = 600
print("__________________________________________________________")
print("welcome to your depleted bank account!!!")
while (money) != -2000:
    print(money)
    R1.clear()
    R2.clear()
    R3.clear()
    play = input(" would you like to play? ")
    if play.lower() == "no":
        break
    if play.lower() != "yes":
        continue
    if play.lower() == "yes":
        money -= play_cost
#check for validation

   
    R1.append(random.randint(0, 9))
    R1.append(random.randint(0, 9))
    R1.append(random.randint(0, 9))
   
    R2.append(random.randint(0, 9))
    R2.append(random.randint(0, 9))
    R2.append(random.randint(0, 9))
   
    R3.append(random.randint(0, 9))
    R3.append(random.randint(0, 9))
    R3.append(random.randint(0, 9))

    print("play.lower is: " + play)
    print(R1)
    print(R2)
    print(R3)
    #__________________________________________
    #payout
    if R1[0] == R1[1] == R1[2]:
        money += Payout
        print(f"you've won {Payout}")
    if R2[0] == R2[1] == R2[2]:
        money += Payout
        print(f"you've won {Payout}")
    if R3[0] == R3[1] == R3[2]:
        money += Payout
        print(f"you've won {Payout}")
#special cases
    if R1[0] == R2[1] ==R3[2]:
        money += Payout
        print(f"you've won {Payout}")
    if R1[2] == R2[1] ==R3[0]:
        money += Payout
        print(f"you've won {Payout}")
#____________________________________________________________________

print(f"you've gotten yourself {money} Dollars")
if money < 0:
    print(f"congrats you are in {money} dollors in debt.")

    #noice