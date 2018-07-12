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
list = []
for letter in word:
    list.append(letter)
print "Welcome to the game Hangman!"
print "I am thinking of a word that is", len(word), "letters long"
var = string.lowercase

guesses = 8
guess_list = []
for item in list:
    guess_list.append(" _ ")
counter = 0
end = 0
while end == 0:
    if guesses == 0:
        break
    elif guess_list == list:
        break
    print "Available letters: " + ''.join(var)
    print "You have ", guesses, " guesses left"
    user_guess = raw_input("Please guess a letter: ")
    answer = 0
    counter = 0
    for item in list:
        if user_guess == item:
            guess_list[counter] = user_guess
            var = var.replace(user_guess, "")
            answer = 1

        elif user_guess != item:
            var = var.replace(user_guess, "")
        counter = counter + 1

    if answer == 1:
        print "Good guess: " + ''.join(guess_list)

    elif answer == 0:
        print "Oops! That letter is not in my word: " + ''.join(guess_list)
        guesses = guesses - 1

if guesses == 0:
    print "Game over, you ran out of guesses. The word was " + word
else:
    print "Congratulations, you won!"















