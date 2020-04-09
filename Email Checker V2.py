import re  # Need this module
# Actually tried
# Official version
def allowed(email_address):
    if not re.search("[^A-Za-z0-9@.,_-]", email_address):  # The allowed characters in an email
        return True  # If the characters are all allowed, then it's returned as True
    else:
        return False  # If not, returns False


def special(first_index, last_index):  # This checks to see if any of the special chars are at the beginning or end
    if not re.search("[^-,_.]", first_index):  # Checks to see if the first character is a special or not
        return False  # If it is a special character, False is returned
    else:
        if not re.search("[^,.-_]", last_index):  # Checks the last character in the email
            return False  # False is returned if the last character is a special character
        else:
            return True  # True is only returned if both the start and the end of the email are alphanumeric chars


def double(email_address):  # This checks to see if any special characters are used consecutively
    for i in range(0, length - 1):  # Loop ends when all consecutive characters have been checked
        if not re.search("[^-,._@]", email_address[i]) and email_address[i] == email_address[i + 1]:
            return False  # If there are 2 consecutive characters that are special, returns False
        else:
            if i == length - 2:  # Otherwise, this function will also check if there's another "@"
                for j in range(0, length):
                    if email_address[j] == "@" and j != index:
                        return False
                    else:
                        pass
                return True
            else:
                pass


x = 0

while x == 0:  # x will stay as 0 until a valid email address is typed, allowing multiple attempts
    email = input("Enter a valid email address:")
    length = len(email)  # Length of the email
    index = email.find('@')  # Where the "@" character is placed
    domain = length + 1 - index
    if index == 0 or index == -1 or index == length - 1:  # Checks to see if the "@" symbol is at the start or the end
        print("Invalid Email")
    elif index > 63 or domain > 255:  # Checks the length of the local and domain part of the email
        print("Invalid Email")
    elif not allowed(email) or not special(email[0], email[length - 1]):  # Checks to see if false was returned at all
        print("Invalid Email")
    elif not double(email):     # Checks if any false was returned for the double function
        print("Invalid Email")
    else:       # Everything is True and therefore a valid email
        print("Valid Email")
        x = 1
