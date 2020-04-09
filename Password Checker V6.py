import re   # Bread & Butter module


def caps(pass1):       # Function to check if there are any uppercase characters
    for i in range(0, word_length):     # Loops the same number of times as the length of the password
        if pass1[i].isupper():      # Checks each character from start to end, to see if any are uppercase
            return True     # If the current character is uppercase, True is returned
        else:
            pass    # If it isn't, then the next character is checked
    return False    # If there isn't any, then False is returned


def lower(pass1):   # Function that checks if the string has any lowercase letters
    for i in range(0, word_length):
        if pass1[i].islower():      # Checks each character from start to end, to see if any are lowercase
            return True
        else:
            pass
    return False


def number(pass1):      # Function that checks if the string has any numbers
    for i in range(0, word_length):
        if pass1[i].isdigit():      # Checks each character from start to end, to see if there are any numbers
            return True
        else:
            pass
    else:
        return False


def letter():       # Function that checks the if the length of the password is acceptable
    if 129 > word_length > 7:       # If it's within that range
        return True         # Returns True
    elif word_length > 128:         # If it's not within the acceptable range, checks to see if it's too long
        return "Too Long"       # If so, returns "Too Long"
    else:
        return "Too Short"      # Otherwise, it must be too short so it returns that


def special(pass1):     # Function that determines if all of the characters are valid
    if not re.search("[^A-Za-z0-9]", pass1):    # Line that actually checks using the regex module
        return True     # If there aren't any special characters, returns True
    else:
        return False    # You could probably guess by this point


y = 0       # I use random variables a lot, they are necessary

while y == 0:      # It will stay as 0 until an accepted password is entered, therefore looping the entire section below
    password = input("Enter Password that contains:\n8-128 characters\nAt least one uppercase & lowercase character\nAt least one digit\nOnly alphanumeric characters:")     # What someone would read
    word_length = len(password)     # Length of the password they entered
    hidden_pass = "*" * word_length     # Me being extra
    n = 1

    if not caps(password):                          # Line 57-74 runs all the functions and prints any errors
        print("No Uppercase Characters")
        n = 0       # If there is an error, n = 0
    if not lower(password):
        print("No Lowercase Characters")
        n = 0
    if not number(password):
        print("No Numeric Characters")
        n = 0
    if letter() == "Too Long":
        print("Too Long")
        n = 0
    if letter() == "Too Short":
        print("Too Short")
        n = 0
    if not special(password):
        print("Contains Special Characters")
        n = 0
    if not n:   # If n = 0, your asked for a password and the code runs again until n = 1
        pass
    else:       # If n = 1(or anything else technically)
        print("Your password:" + hidden_pass + " is valid.")    # You're told your password has been accepted
        y = 1       # This stops the code from looping
# Changed, tried something new, and as far as I remember, this works with a few minor logic errors
