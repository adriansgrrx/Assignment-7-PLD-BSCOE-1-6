# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

"""
Regular Expression (RegEx) module will be used in this program
"""
import re   # regex module

password = input("enter ur pass: ")
if (len(password) > 15):
    print("Ok good")
else:  
    print("bad")