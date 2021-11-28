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
Regular Expression (regex) module will be used in this program
"""
import re   # regex module

# while functionality for looping
while True:
    # Ask for the user input
    password = input("\nEnter your password: ")
  
    # f-elif statements section
    if (len(password) < 15): # len functionality to determine the length of the input then compete with the integer 15(standard char input)
        print("\n[Invalid Input]\nPassword must be 15 charcters and above.\n") # if not satisfied, display.
        """
        from regular exp. module, .search(pattern, string) command is used to scan/search character(s) inside the string/list
        """
    # I used [] to indicate list.
    elif re.search(r"[A-Z]", password)is None:  # "r" is used to modify "raw-string" and 'is None' is provided if it does not contain the charcters
        print("\n[Password Status: Weak]\nInclude Capital Letters [A-B-C] in your password.\n") # if not satisfied, display.
    elif re.search(r"[a-z]", password)is None: # " "
        print("\n[Password Status: Weak]\nInclude Small Letters [a-b-c] in your password.\n") # if not satisfied, display.
    elif re.search(r"\d", password)is None: # '\d' special char to indicate digits/ numbers 0-9
        print("\n[Password Status: Weak]\nInclude Numbers or Digits [0-9] in your password.\n") # if not satisfied, display.
    elif re.search(r"[!@#$%^&*()_+]", password)is None:
        print("\n[Password Status: Weak]\nInclude Special Characters [!@#$%^&*()_+] in your password.\n") # if not satisfied, display.
        
        """
        from regular exp. module, .match(pattern,string, flag = 0) command is used to compare or 
        simply match the 'password'(string/varriable) to a 'format'(pattern).
        """
    elif re.match(r"[a-z A-Z 0-9 !@#$%^&*()_+]{15}", password): # match the string to a pattern/variable including 'r'= raw-string and 15 which is the standard number of the password.
        format = re.compile(r"[a-z A-Z 0-9 !@#$%^&*()_+]{15}") # .compile() to compile regular exp. objects
        result = format.match(password) 
        print("\n[Password Status: Strong]\nValid password!\n") #display if satisfied
        break 
        # End of the program, incase the condition satisfied.
        """
    In this section, the else statement will only function if the following 
    input didn't match any of the condition.
        """
    else:
        print("\n[Invalid Password]\nPassword Criteria:\n> Greater than 15 letters.\n> Have at least one capital letter.\n> Have at least one number.\n> Have at least one special character (!@#$%^&*()_+ etc)\n")
    # the loop will take over...    