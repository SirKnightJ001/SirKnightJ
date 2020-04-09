import re  # Bread & Butter module


# At this point, a lot of my notes will be copied, as they go along with the line they're coincided with
# My latest Password Checker
def caps(pass1):  # Function to check if there are any uppercase characters
    for k in range(word_length):  # Loops the same number of times as the length of the password
        if pass1[k].isupper():  # Checks each character from start to end, to see if any are uppercase
            return True  # If the current character is uppercase, True is returned
        else:
            pass  # If it isn't, then the next character is checked
    errors.append("No Uppercase Character")
    return False  # If there isn't any, then False is returned


def lower(pass1):  # Function that checks if the string has any lowercase letters
    for j in range(word_length):
        if pass1[j].islower():  # Checks each character from start to end, to see if any are lowercase
            return True
        else:
            pass
    errors.append("No Lowercase Character")
    return False


def number(pass1):  # Function that checks if the string has any numbers
    for b in range(word_length):
        if pass1[b].isdigit():  # Checks each character from start to end, to see if there are any numbers
            return True
        else:
            pass
    errors.append("No Numeric Characters")
    return False


def letter():  # Function that checks the if the length of the password is acceptable
    if 129 > word_length > 5:  # If it's within that range
        return True  # Returns True
    elif word_length > 128:  # If it's not within the acceptable range, checks to see if it's too long
        errors.append("Too Long")
        return False  # If so, returns False
    else:
        errors.append("Too Short")
        return False  # Otherwise, it must be too short so it returns that


def special(pass1):  # Function that determines if all of the characters are valid
    if not re.search("[^A-Za-z0-9]", pass1):  # Line that actually checks properly using the regex module
        return True  # If there aren't any special characters, returns True
    else:
        print("Contains Special Characters")
        return False  # You could probably guess by this point


y = 0  # I use random variables a lot, they are necessary

while y == 0:  # It will stay as 0 until an accepted password is entered, therefore looping the entire section below
    password = input("Enter Password that contains:\n6-128 characters\nAt least one uppercase & lowercase character\nAt least one digit\nOnly alphanumeric characters:")  # What someone would read
    word_length = len(password)  # Length of the password they entered
    hidden_pass = "*" * word_length  # Me being extra
    errors = []
    n = 1
    caps(password)
    lower(password)
    number(password)
    letter()
    special(password)
    if errors:      # If the list 'errors' isn't empty
        for i in range(len(errors)):
            print(errors[i])
    else:  # Spectacular compared to V2
        print("Valid Password")  # Congrats
