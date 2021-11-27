# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8
"""
time module will be used in this program
""" 
import time

# Ask for a text input
yourSentence = input("\nType or paste the text you wish to be analyze:\n")
def get_calculation(): # def functionality
    # essential global variables
    wordC = 0   # wordC = Word count
    vowelC = 0      # vowelC = Vowel count
    consonantC = 0      # consonantC = Consonant count
    # additional secondary text information
    spaceC = 0     # spaceC=  Space count
    charC = 0   #charC = Character count
    # List of the assignments stored in a variable
    consonants = ["b","B","c","C","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
    vowels = ["a","A","e","E","i","I","o","O","u","U"]