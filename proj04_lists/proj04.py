# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

# var = ["a", "b", "cat", 3]
# #index
# print var[0]
# #slice of list
# print var[0:3]
# #all but first
# print var[1:]
# #all but last
# print var[:-1]
# #replace
# var[0] = "tree"
# print var
# #loop
# #to change
# counter = 0
# for item in var:
#     if item == "cat":
#         var[counter] = "dog"
#     elif item == "tree":
#         var[counter] = "flower"
#     counter = counter + 1
# print var
# #to add on the end of a list
# var.append(28)
# print var
# #to split a string into a list
# lst = []
# s = "This is a string"
# for letter in s:
#     lst.append(letter)
# print lst
#
# new_lst = []
# for item in a:
#     if item < 5:
#         print item
#         new_lst.append(item)
#
# print new_lst
# compare = raw_input("Enter a number: ")
# compare = int(compare)
# new_lst2 = []
# for item in a:
#     if item < compare:
#         new_lst2.append(item)
# print new_lst2






#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# lst = []
# for item in a:
#     if item in b:
#         if item not in lst:
#             lst.append(item)
# print lst






#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
# counter = 0
# for item in d:
#     if item == "a":
#         d[counter] = "*"
#     counter = counter + 1
# print d











#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

s = raw_input("Enter a word or expression: ")
s_show = s
s = s[0:].lower()
lst = []
counter = 0
for letter in s:
    lst.append(letter)
for item in lst:
    if item == " ":
        lst.remove(item)
for item in range(len(lst)):
    if len(lst) == 0:
        break
    elif lst[0] == lst[-1]:
        lst = lst[1:-1]
    counter = counter + 1
if len(lst) <= 1:
    print s_show + " is a palindrome"
else:
    print s_show + " is not a palindrome"









