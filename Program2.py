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

# Ask for the user input
password = input("enter ur pass: ")

# f-elif statements section
if (len(password) < 15)is None: # len functionality to determine the length of the input then compete with the integer 15(standard char input)
    print("passsword must be 15 characters and above") # if satisfied, display.

    """
from regular exp. module, .search(pattern, string) command is used to scan/search character(s) inside the string/list
    """
# I used [] to indicate list.
elif re.search(r"[A-Z]", password)is None:  # "r" is used to modify "raw-string" and 'is None' is provided if it does not contain the charcters
    print("password must contain Capital letters")
elif re.search(r"[a-z]", password)is None: # " "
    print("password must contain Small letters") # " "
elif re.search(r"\d", password)is None: # '\d' special char to indicate digits/ numbers 0-9
    print("password mus have D")
elif re.search(r"[!@#$%&]", password)is None:
    print("password must have SChar")
elif re.search(r"[a-z A-Z 0-9 !@#$%&]", password): # sum-p all the input to proceed on valid password
    print("Valid password!")