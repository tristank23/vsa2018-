# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)
print word
list = []
for letter in word:
    list.append(letter)
print "Welcome to the game Hangman!"
print "I am thinking of a word that is", len(word), "letters long"
var = string.lowercase

guesses = 8
guess_list = []
for item in list:
    guess_list.append("_")
counter = 0
while True:
    print "Available letters: " + ''.join(var)
    print "You have ", guesses, " guesses left"
    user_guess = raw_input("Please guess a letter: ")
    answer = False

    for item in list:
        counter = 0
        if user_guess == item:
            guess_list[counter] = user_guess
            var = var.replace(user_guess, "")
            answer = True

        elif user_guess != item:
            guesses = guesses - 1
            var = var.replace(user_guess, "")
        elif guess_list == list:
            print "Congrats you won!!!"
        counter = counter + 1
    if answer == True:
        print "Good guess: " + ''.join(guess_list)
    elif answer == False:
        print "Oops! That letter is not in my word: " + ''.join(guess_list)














