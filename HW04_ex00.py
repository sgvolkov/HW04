#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports

import random

# Body   

nr_correct = random.randrange(1,26)

for i in range(5):
    try:
        nr = int(raw_input("Guess the # I'm thinking of. It's between 1 - 25 "))
    except:
        ValueError
        print "That's not a number! Try again"
        continue
    if nr == nr_correct:
        print "Congrats!"
        break
    elif nr > nr_correct:
        print "Too high, try again"
    elif nr < nr_correct:
        print "Too low, try again"

print 'the right answer was %d' % nr_correct

################################################################################
def main():

if __name__ == '__main__':
    main()
