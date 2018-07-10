# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

# key word is for

# loop over a range of #s
#
# for num in range (51):
#     sum = sum + num
#     print sum
#
# s = "vsa"
# #loop over strings
# for letter in s:
#     print letter
#     if letter == "s":
#         print "This is an s"

stop = raw_input("How many Fibonacci numbers would you lke to generate? ")
stop = int(stop)
num = 0
prev_num = 0
current_num = 1


for num in range(stop):
    print current_num
    next_num = current_num + prev_num
    prev_num = current_num
    current_num = next_num
    num = num + 1

