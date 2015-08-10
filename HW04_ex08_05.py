#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

def count(word, letter):
	cat = word
	count_letters = 0
	for char in cat:
            if char == letter:
                count_letters = count_letters + 1
	print count_letters


################################################################################
def main():

    count('hello', 'l')
    count('dingbat', 'g')

if __name__ == '__main__':
    main()
