# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random
print "This game is designed for 2 players."
user_name = raw_input("Please enter your name: ")
print "I'm thinking of a number between 1 and 9. Can you guess my number?"
correct_num = random.randint(1,9)
user_points = 1
user_coins = 15
while True:
    user_guess = raw_input("Enter a number, or 'exit' to end the game: ")
    if user_guess == "exit":
        print "You have exited the game. Game Over"
        break
    elif int(user_guess) == int(correct_num):
        print "Congratuations, you guessed my number! You used", int(user_points), "guess(es). You have", int(user_coins), "points."
        break
    elif int(user_points) >= 3:
        user_coins = int(user_coins) - 5
        print "You ran out of guesses. Game Over. You have 0 points"
        break
    elif int(user_guess) > int(correct_num):
        print "Your number is too high."
        user_points = int(user_points) + 1
        user_coins = int(user_coins) - 5
    elif int(user_guess) < int(correct_num):
        print "Your number is too low."
        user_points = user_points + 1
        user_coins = int(user_coins) - 5

import random
user_name2 = raw_input("Please enter your name: ")
print "I'm thinking of a number between 1 and 9. Can you guess my number?"
correct_num2 = random.randint(1,9)
user_points2 = 1
user_coins2 = 15
while True:
    user_guess2 = raw_input("Enter a number, or 'exit' to end the game: ")
    if user_guess2 == "exit":
        print "You have exited the game. Game Over"
        break
    elif int(user_guess2) == int(correct_num2):
        print "Congratuations, you guessed my number! You used", int(user_points2), "guess(es). You have", int(user_coins2), "points."
        break
    elif int(user_points2) >= 3:
        user_coins2 = int(user_coins2) - 5
        print "You ran out of guesses. Game Over. You have 0 points"
        break
    elif int(user_guess2) > int(correct_num2):
        print "Your number is too high."
        user_points2 = int(user_points2) + 1
        user_coins2 = int(user_coins2) - 5
    elif int(user_guess2) < int(correct_num2):
        print "Your number is too low."
        user_points2 = user_points2 + 1
        user_coins2 = int(user_coins2) - 5
if int(user_coins) > int(user_coins2):
    print "Congratulations " + user_name + ", you beat " + user_name2 + "by", int(user_coins) - int(user_coins2), "points."
elif int(user_coins) < int(user_coins2):
    print "Congratulations " + user_name2 + ", you beat " + user_name + "by", int(user_coins2) - int(user_coins), "points."
elif int(user_coins) == int(user_coins2):
     print "Congratulations " + user_name + " and " + user_name2 + ", you tied!"