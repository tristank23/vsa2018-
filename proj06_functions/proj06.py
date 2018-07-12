# Name:
# Date:

# proj05: functions and lists

# def adder(x,y):
#     z = x + y
#     return z
#
# #call a function
# print adder(3,5)




# Part I

def divisors(num):
    """
    Takes a number and returns all divisors of the number, ordered least to greatest
    :param num: int
    :return: list (int)
    """

    # Fill in the function and change the return statment.

#     lst = []
#     for item in range(1, num + 1):
#         if num % item == 0:
#             lst.append(item)
#     return lst
# print divisors(8)

def prime(num):
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """

    # Fill in the function and change the return statment.

#     prime_lst = [1, num]
#     lst = []
#     for item in range(1, num + 1):
#         if num % item == 0:
#             lst.append(item)
#     if lst == prime_lst:
#         return True
#     else:
#         return False
# print prime(5)






# Part II:
# REVIEW: Conditionals, for loops, lists, and functions
#
# INSTRUCTIONS:
#
# 1.  Make the string "sentence_string" into a list called "sentence_list" sentence_list
# should be a list of each letter in the string: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm',
# 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'M', 'o', 'n', 't', 'y', ' ', 'P',
# 'y', 't', 'h', 'o', 'n', '.']
#
# Hint: Use a for loop and with an append function: list.append(letter)
#
sentence_string = "Hello, my name is Monty Python."
sentence_list = []
for letter in sentence_string:
    sentence_list.append(letter)
print sentence_list






# 2. Print every item of sentence_list on a separate line using a for loop, like this:
# H
# e
# l
# l
# o
# ,
#
# m
# y
#  .... keeps going on from here.

for item in sentence_list:
    print item




# 3: Write a for loop that goes through each letter in the list vowels. If the current
# letter is 'b', print out the index of the current letter (should print out the
# number 1).
#
vowels = ['a', 'b', 'i', 'o', 'u', 'y']

counter = 0
for item in vowels:
    if item == 'b':
        print counter
    counter = counter + 1




# 4: use the index found to change the list vowels so that the b is replaced with an e.

counter = 0
for item in vowels:
    if item == 'b':
        vowels[counter] = 'e'
    counter = counter + 1
print vowels





# 5: Loop through each letter in the sentence_string. For each letter, check to see if the
#  number is in the vowels list. If the letter is in the vowels list, add one to a
# counter. Print out the counter at the end of the loop. This counter should show how
# many vowels are in sentence_string.

counter1 = 0
for letter in sentence_string:
    if letter in vowels:
        counter1 = counter1 +  1
print counter1



# 6: Make a new function called "vowelFinder" that will return a list of  the vowels
# found in a list (no duplicates).The function's parameters should be "list" and "vowels."


#  Example:
# vowelList = vowelFinder(sentence_list, vowels)
# print vowelList

# ['a', 'e', 'i', 'o', 'y']

def vowel_finder(sentence_list, vowels):
    vowel_list = []
    for item in sentence_list:
        if item in vowels:
            if item not in vowel_list:
                vowel_list.append(item)
    return vowel_list
vowelList = vowel_finder(sentence_list, vowels)
print vowelList