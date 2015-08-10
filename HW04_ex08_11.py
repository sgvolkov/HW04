#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False
#this seems to work unless you start with a whitespace, in which case you get
#a false False.

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
#Wrong. this is only looking at 'c' as it's written in the if statement, so it will
#always be True.

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        flag = c.islower()
    return flag

#This only returns the value once it's complete, so you only get the value of
#the last lowercase character.

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#This will return either True or False.

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """
    for c in s:
        if not c.islower():
            return False
    return True

#If any character is not lowercase, it'll return False. 

################################################################################
def main():

    any_lowercase1("workswithoutwhitespaces")
    any_lowercase2("isalwaystrue")
    any_lowercase3("onlyvalueoflastlowercasecharacter")
    any_lowercase4("returnstrueorfalse")
    any_lowercase5("allcharactershavetobelowercase")
    

if __name__ == '__main__':
    main()
