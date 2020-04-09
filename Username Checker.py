import re  # Bread & butter module


def special(user_name):  # The allowed characters in an username
    if not re.search("[^A-Za-z0-9._-]", user_name):  # Searches the string, to see if there are any illegal chars
        return True  # If not
    else:                                       # Story ____ Music Videos beat _____ Music Videos in my opinion
        return False                            # More emotion


y = 0  # My random variable would usually be y it seems, instead of x(there isn't a difference). Maybe in this case.

while y == 0:  # Getting bored of writing comments, I really recommend watching:(Marvel) Avengers|A soul for a soul. Speaking out to any marvel fan
    username = input("Enter a username:")  # Person enters their username
    length = len(username)  # Length of entered username
    if special(username) == True and 13 > length > 3:  # If there aren't special chars and it fits the length range
        print("Valid Username")  # Valid
        y = 1  # I want to sleep(midnight) but this is important to me
    elif special(username):  # Checks to see if the problem is that there are special characters
        print("Invalid.Has to be between 4-12 characters.")  # If that isn't the problem, then it must be the length
    elif 13 > length > 3:  # Checks to see if the length is the problem
        print("Invalid.Can't contain specific special characters.")  # If not, there must be an illegal character
    else:  # If they are both problems(too short/long and contains special characters), below's printed
        print("Invalid.Has to be between 4-12 characters & it can't contain specific special characters.")
# I did slightly change this in my final script