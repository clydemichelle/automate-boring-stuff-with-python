#! python3

#passwordStrengthDetection.py - Checks on the strength of the password based on users input

#Import necessary modules
import re

def passwordChecker(password):
    passwordRegex = re.compile(r'''( ^
    (.[A-Za-z]+)?
    (.\d)?
    [a-zA-Z\d]
    {8,}
    $)''',re.VERBOSE)

    strength = passwordRegex.search(password)
    if strength :
        print('Strong Password, Well Done.')
    else:
        print('Weak Password, Try again')

print("""
        Enter your password to check it\'s strength.
        The Rules:
        At least 8 characters long
        Contains both uppercase and lowercase characters
        At least one digit
        """)
password = input()
passwordChecker(password)
