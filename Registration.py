import re  # Now my Bread & Butter module
import time  # This module is just for fun


def email_allowed(email_address):       # This checks if there are any unpermitted characters in the entered email
    if not re.search("[^A-Za-z0-9@.,_-]", email_address):  # The email_allowed characters in an email
        return True  # If the characters are all email_allowed, then it's returned as True
    else:
        return False  # If not, returns False


def index_special(first_index, last_index):  # Checks if any of the special characters are at the beginning & end
    if not re.search("[^-,_.]", first_index):  # Checks to see if the first character is a index_special or not
        return False  # If it is a special character, False is returned
    else:       # OMG I watching the first eps now of Akame Ga Kill, quite shocked! It was only a recommendation because I like close-range, sword-style combat, but I'm finishing it today.
        if not re.search("[^,.-_]", last_index):  # Checks the last character in the email
            return False  # False is returned if the last character is a special character
        else:
            return True  # True is only returned if both the start and the end of the email are alphanumeric chars


def double(email_address):  # This checks to see if any special characters are used consecutively
    for i in range(length - 1):  # Loop ends when all consecutive characters have been checked
        if not re.search("[^-,._@]", email_address[i]) and email_address[i] == email_address[i + 1]:
            return False  # If there are 2 consecutive characters that are special, returns False
        else:
            if i == length - 2:  # Otherwise, this function will also check if there's another "@"
                for j in range(length):
                    if email_address[j] == "@" and j != index:      # This checks each character for any other '@'
                        return False        # If there's more than one, return's False
                    else:
                        pass
                return True
            else:
                pass


def special_name(user_name):  # The allowed characters in an username
    if not re.search("[^A-Za-z0-9._-]", user_name):  # Searches the string, to see if there are any illegal characters
        return True  # If not
    else:
        return False  # If so


def duplicate_email(email_address):         # This function checks for any other duplicate emails
    accounts_read = open("accounts.txt", "r").readlines()       # The entire document is equal to this(turned into a list, line by line)
    total_lines = len(accounts_read)            # Number of lines in the copied file
    for i in range(total_lines):                # Runs up to the number of lines
        current_line = accounts_read[i]         # Current line becomes equal to the line depending on the number of times it's looped, I don't have to go in detail
        line_length = len(current_line)         # The length of current line
        last = line_length - 1 - current_line[::-1].index(" ")      # Last is basically equal to the second space in the line, separating the password and the email
        registered = current_line[last + 1:line_length - 1]         # Registered is equal to the email registered
        if email_address.lower() == registered.lower():             # All the characters are lowered for both the registered email, & the entered email
            accounts_read.close()
            return False        # If they are the same, returns false
    return True                 # If all the emails in each line are different to the entered email, True is returned, as there aren't any copies


def duplicate_name(user_name):      # Slightly different from the duplicate email_address function
    accounts_read = open("accounts.txt", "r").readlines()
    total_lines = len(accounts_read)
    for i in range(total_lines):
        current_line = accounts_read[i]
        first = current_line.index(" ")     # The first space, between the username & password
        registered = current_line[:first]
        if user_name.lower() == registered.lower():
            return False
    return True


def caps(pass1):  # Function to check if there are any uppercase characters
    for k in range(word_length):  # Loops the same number of times as the length of the password
        if pass1[k].isupper():  # Checks each character from start to end, to see if any are uppercase
            return
        else:
            pass  # If it isn't, then the next character is checked
    errors.append("No Uppercase Character")


def lower(pass1):  # Function that checks if the string has any lowercase letters
    for j in range(word_length):
        if pass1[j].islower():  # Checks each character from start to end, to see if any are lowercase
            return
        else:
            pass
    errors.append("No Lowercase Character")


def number(pass1):  # Function that checks if the string has any numbers
    for i in range(word_length):
        if pass1[i].isdigit():  # Checks each character from start to end, to see if there are any numbers
            return
        else:
            pass
    errors.append("No Numeric Characters")


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
    if not re.search("[^A-Za-z0-9]", pass1):  # Line that actually checks using the regex module
        return      # There isn't a need to return anything, but something has to be returned anyway
    else:
        print("Contains Special Characters")


def confirm(user1, pass1):      # This function is used to check if the username and password entered, are valid to your account's details
    file_read = open("accounts.txt", "r").readlines()
    for i in range(len(file_read)):
        current_line = file_read[i]
        first = current_line.find(" ")
        last = len(current_line) - 1 - current_line[::-1].find(" ")
        if user1 == current_line[:first]:           # If the username is correct in a line
            if pass1 == current_line[first + 1:last]:       # If the password is correct in the same line
                file_read.close()
                return True         # True is returned
            else:               # Anything else & false is returned
                pass
    return False


def verify(email_address):              # Verification of your entered email
    file_read = open("accounts.txt", "r").readlines()
    for i in range(len(file_read)):
        current_line = file_read[i]
        first = current_line.find(" ")
        last = len(current_line) - 1 - current_line[::-1].find(" ")
        if email_address == current_line[last + 1:len(current_line) - 1]:
            print("Enter the six digit code sent to your email:")  # Imagine if I knew the entered email accounts
            time.sleep(2)  # As the person comes to terms with the fact that I know their email
            print("jk\nYour password is:" + current_line[first + 1:last] + ".")  # Relieved that it was a joke
            file_read.close()
            return True
    return False


def actual(user_name):          # Given that someone only needs to enter their username & password to log in, this checks for that user's email
    file_read = open("accounts.txt", "r").readlines()
    for i in range(len(file_read)):
        current_line = file_read[i]
        length2 = len(current_line)
        first = current_line.find(" ")
        last = len(current_line) - 1 - current_line[::-1].find(" ")
        if user_name == current_line[:first]:       # Using that player's username, finds the line in which that username is stored
            file_read.close()
            return current_line[last + 1:length2 - 1]       # Returns that players email in the same line


def new_email(email_address):           # If someone want's to enter a new email, this function is supposed to replace the old email with the new one entered[email_address]
    file_read = open("accounts.txt", "r").readlines()
    file_append = open("accounts2.txt", "a")            # All my 'new' functions that aim to replace an old credential with a new, copy all the contents from the official file into a temporary one
    global player_user              # Player's username
    global player_pass              # Player's password
    for i in range(len(file_read)):
        current_line = file_read[i]
        first = current_line.find(" ")
        if player_user == current_line[:first]:     # Finds the line in which the username's are the same
            file_append.write(player_user + " " + player_pass + " " + email_address + "\n")         # Re enters the username, password, and the new email
        else:
            file_append.write(current_line + "\n")      # Otherwise, it just rewrites the line from the original to the temporary
    file_append.close()


def new_user(user_name):        # Same as the above function except it's a new username, minor changes
    file_read = open("accounts.txt", "r").readlines()
    file_append = open("accounts2.txt", "a")
    global player_pass
    global player_email
    for i in range(len(file_read)):
        current_line = file_read[i]
        first = current_line.find(" ")
        if player_user == current_line[:first]:
            file_append.write(user_name + " " + player_pass + " " + player_email + "\n")
        else:
            file_append.write(current_line + "\n")
    file_append.close()


def new_pass(pass1):        # Same as the above except it's a password replacement, minor changes
    file_read = open("accounts.txt", "r").readlines()
    file_append = open("accounts2.txt", "a")
    global player_user
    global player_email
    for i in range(len(file_read)):
        current_line = file_read[i]
        first = current_line.find(" ")
        if player_user == current_line[:first]:
            file_append.write(player_user + " " + pass1 + " " + player_email + "\n")
        else:
            file_append.write(current_line + "\n")
    file_append.close()


def rewrite():          # This function copies the text from the temp file to the actual file
    temp = open("accounts2.txt", "r").readlines()
    line_length = len(temp)
    with open("accounts.txt", "w") as f1:
        for k in range(0, line_length):
            line = temp[k]
            print("z")
            f1.write(line)
    open("accounts2.txt", "w").close()      # This clears anything from the temp file


def line_delete():              # This deletes any unnecessary lines[empty spaces] from the first line
    file_read = open("accounts.txt", "r").readlines()       # Equal to the file
    file_length = len(file_read)
    file_list = file_read       # Also, equal to the file
    temp = False
    for i in range(1, file_length):
        specific_line = file_read[file_length - i]
        if specific_line == "\n":  # specific_line[0:2:-1] == "\n" or specific_line[0:2:-1] == "n\\": was originally my line of code(edited multiple times), but it didn't want to work for whatever reason, and it's unimportant anyway, just an idea
            file_list.remove("\n")      # Removes the empty lines
            temp = True
        else:
            if temp:            # If temp == True
                file_write = open("accounts.txt", "w")
                file_write.writelines(file_list)        # Rewrites the file without the empty lines


#   w, x, y, z = 0, 0, 0, 0  I thought I needed this many variables
a = 0  # Realized that I only needed one

make = open("accounts.txt", "a")            # This creates both of the files if they aren't already saved in the locally
make.write("")
make.close()
make = open("accounts2.txt", "a")
make.write("")
make.close()

print("Type 'end' at any point to exit the program.\nType 'back' to return to the previous instruction/question.\nType 'redo' to come back to this stage of the program.")

while a == 0:           # The variable, 'a' represents stages in the code
    line_delete()           # Just to make sure there aren't any unneeded lines
    decision = input("Do you want to 'Register' or 'Log In':")          # What do you want to do? Your choice
    decision = decision.lower()  # Case-insensitive
    if decision == "register" or decision == "sign up" or decision == "create an account" or decision == "reg":  # Being extra
        a = 1
        while a == 1:
            email = input("Enter a valid email address:")  # User enters their email
            length = len(email)  # Length of the email
            index = email.find('@')  # Where the "@" character is placed or if there is one
            index2 = email.find(".")  # Where the "." character is placed if there is one
            domain = length + 1 - index
            if length == 0:
                print("You need to enter an email in case you forget your password")
            elif email.lower() == "end":
                exit()
            elif email.lower() == "back" or email.lower() == "redo":
                a = 0
            elif index == 0 or index == -1 or index == length - 1:  # Sees if the "@" symbol is at the start or the end
                print("Invalid Email")                    # Given that your email shouldn't be made up, I see no reason to tell the reason why it's email
            elif index2 == 0 or index2 == -1 or index2 == length - 1:  # Sees if the "@" symbol is at the start or the end
                print("Invalid Email")
            elif index > 63 or domain > 255:  # Checks the length of the local and domain part of the email
                print("Invalid Email")
            elif not email_allowed(email) or not index_special(email[0], email[length - 1]):  # If false was returned
                print("Invalid Email")
            elif not double(email):  # Checks if any false was returned for the double function
                print("Invalid Email")
            elif not duplicate_email(email):  # Checks if the email has already been registered
                print(email + " has already been registered")  # Valid, but has already been registered
            else:
                print("Type 'specs' to see the criteria your username/password must follow")  # Wasn't my initial plan, but a new, helpful command for you
                a = 2
                while a == 2:
                    username = input("Enter a valid username:")  # Person enters their username
                    length = len(username)  # Length of entered username
                    if username.lower() == "end":           # I'm a bit bored rn
                        exit()
                    elif username.lower() == "specs":                   # All the characters in the username changes to lowercase
                        print("Has to be between 5-12 characters\nCan't contain specific special characters")
                    elif username.lower() == "back":
                        a = 1
                    elif username.lower() == "redo":
                        a = 0
                    elif length == 0:           # If nothing was typed:
                        print("You've got to enter something.")     # I think I only did this for my username
                    elif special_name(username) == False and 13 > length > 4:
                        print("Invalid.Can't contain specific special characters.")
                    elif special_name(username) == True and 5 > length:
                        print("Invalid. Has to be at least 5 characters in length.")
                    elif length > 12 and special_name(username):
                        print("Invalid. The maximum number of characters a username can contain is 12.")
                    elif length > 12 or length < 5 and not special_name(username):
                        print("Invalid.Has to be between 5-12 characters & it can't contain specific special characters.")
                    else:
                        if not duplicate_name(username):
                            print("Username is too similar")
                        else:
                            a = 3
                            while a == 3:
                                password = input("Enter a valid password:")
                                word_length = len(password)  # Length of the password they entered
                                hidden_pass = "*" * word_length  # Me being extra
                                errors = []
                                if password.lower() == "specs":
                                    print("6-128 characters\nAt least one uppercase & lowercase character\nAt least one digit\nOnly alphanumeric characters")
                                elif not word_length:
                                    print("You need a password as a verification.")     # Seems I did this for my password as well
                                elif password.lower() == "end":
                                    exit()
                                elif password.lower() == "back":        # Back deduces 'a'[stage number if it's easier to think of it as that] by 1 - 2 depending on said stage
                                    a = 2
                                elif password.lower() == "redo":        # Well, I'm tired
                                    a = 0
                                else:                       # At this point, the next 5 lines just runs the functions to check if the password meets the criteria or not
                                    caps(password)
                                    lower(password)
                                    number(password)
                                    letter()                # Since I don't use a parameter for the letter function, I feel like it possibly could perform a logic error. I've tried to make sure it won't happen, that the main variable, 'word_length', is always what I want it to be. Still...
                                    special(password)
                                    if errors:
                                        for m in range(len(errors)):
                                            print(errors[m])
                                    else:
                                        print("All your details are valid.")        # Well done, all your details are valid
                                        a = 4
                                        while a == 4:
                                            player_user, player_pass, player_email = username, password, email          # Details get saved into different variables
                                            hidden_pass2 = len(player_pass) * "*"
                                            print("Email:" + player_email + "\nUsername:" + player_user + "\nPassword:" + hidden_pass2)        # Prints all your details(password's hidden though)
                                            a = 5           # That's all this stage does
                                            while a == 5:
                                                credentials = input("Confirm: Would you like to register the details above[Yes/No]:")           # Your options are given
                                                credentials = credentials.lower()               # Your answer turns into all lowercase characters
                                                if credentials == "yes" or credentials == "yeah" or credentials == "ye" or credentials == "affirmative" or credentials == "true" or credentials == "yas" or credentials == "yeh":       # So many options for one word that was given to you, just incase
                                                    new = open("accounts.txt", "a")     # Your details are saved into the file
                                                    new.write("\n" + username + " " + password + " " + email)
                                                    print("Your account has been successfully created\nWelcome " + username)
                                                    time.sleep(5)   # Time before the code ends
                                                    exit()          # And the code ends
                                                elif credentials == "no" or credentials == "false" or credentials == "nope" or credentials == "nah" or credentials == "na":
                                                    a = 6
                                                    while a == 6:
                                                        change = input("Would you like to change your entered 'email','username' or 'password':")       # Someone may want to change their email
                                                        change = change.lower()
                                                        if change == "redo":        # If the 'redo' command is typed, the program essentially starts again
                                                            a = 0
                                                        elif change == "back":
                                                            a = 5
                                                        elif change == "end":
                                                            exit()
                                                        elif change == "email" or change == "email address" or change == "email_address":       # If you want to change your email
                                                            a = 7       # Stage 7
                                                            while a == 7:
                                                                email = input("Enter a valid email address:")  # User enters their email
                                                                length = len(email)  # Length of the email
                                                                index = email.find('@')  # Where the "@" character is placed or if there is one
                                                                domain = length + 1 - index
                                                                if length == 0:
                                                                    print("Obviously Invalid")
                                                                elif email.lower() == "end":
                                                                    exit()
                                                                elif email.lower() == "back":
                                                                    a = 6
                                                                elif email.lower() == "redo":
                                                                    a = 0
                                                                elif index == 0 or index == -1 or index == length - 1:  # Sees if the "@" symbol is at the start or the end
                                                                    print("Invalid Email")
                                                                elif index > 63 or domain > 255:  # Checks the length of the local and domain part of the email
                                                                    print("Invalid Email")
                                                                elif not email_allowed(email) or not index_special(email[0], email[length - 1]):  # If false was returned
                                                                    print("Invalid Email")
                                                                elif not double(email):  # Checks if any false was returned for the double function
                                                                    print("Invalid Email")
                                                                elif not duplicate_email(email):  # Checks if the email has already been registered
                                                                    print(email + " has already been registered")  # Valid, but has already been registered
                                                                else:
                                                                    player_email = email
                                                                    print("Your email has successfully been changed")
                                                                    a = 4
                                                        elif change == "username" or change == "user" or change == "user name":
                                                            a = 7       # Stage 7, even if it's a different path
                                                            while a == 7:
                                                                username = input("Enter a valid username:")  # Person enters their username
                                                                length = len(username)  # Length of entered username
                                                                if username.lower() == "end":
                                                                    exit()
                                                                elif username.lower() == "specs":
                                                                    print("Has to be between 5-12 characters\nCan't contain specific special characters")
                                                                elif username.lower() == "back":
                                                                    a = 6
                                                                elif username.lower() == "redo":
                                                                    a = 0
                                                                elif length == 0:
                                                                    print("You've got to enter something.'")
                                                                elif special_name(username) == False and 13 > length > 4:
                                                                    print("Invalid.Can't contain specific special characters.")
                                                                elif special_name(username) == True and 5 > length:
                                                                    print("Invalid. Has to be at least 5 characters in length.")
                                                                elif length > 12 and special_name(username):
                                                                    print("Invalid. The maximum number of characters a username can contain is 12.")
                                                                elif length > 12 or length < 5 and not special_name(username):
                                                                    print("Invalid.Has to be between 5-12 characters & it can't contain specific special characters.")
                                                                elif not duplicate_name(username):
                                                                    print("Username is too similar")
                                                                else:
                                                                    player_user = username
                                                                    print("Your username has successfully been changed")
                                                                    a = 4
                                                        elif change == "password" or change == "pass":
                                                            a = 7
                                                            while a == 7:
                                                                password = input("Enter a valid password:")
                                                                word_length = len(password)
                                                                hidden_pass = "*" * word_length
                                                                errors = []
                                                                if password.lower() == "specs":
                                                                    print("6-128 characters\nAt least one uppercase & lowercase character\nAt least one digit\nOnly alphanumeric characters")
                                                                elif word_length == 0:
                                                                    print("You need a password as a verification.")
                                                                elif password.lower() == "end":
                                                                    exit()
                                                                elif password.lower() == "back":
                                                                    a = 6
                                                                elif password.lower() == "redo":
                                                                    a = 0
                                                                else:
                                                                    caps(password)
                                                                    lower(password)     # I started slacking when encountering problems(mainly due to the number of hours I've previously wasted trying to fix others), which is why I'm posting this 1.5 weeks later
                                                                    number(password)
                                                                    letter()
                                                                    special(password)
                                                                    if errors:
                                                                        for m in range(len(errors)):
                                                                            print(errors[m])
                                                                    else:
                                                                        player_pass = password
                                                                        print("Your password has now been changed")
                                                                        a = 4
                                                elif credentials == "end":
                                                    exit()
                                                elif credentials == "back":
                                                    a = 4
                                                    print("In this case, typing 'back' would reveal your entered details again")
                                                elif credentials == "redo":
                                                    a = 0
                                                else:
                                                    if len(credentials) > 0:
                                                        print("That wasn't an answer I would anticipate someone to write so...umm, just write something else that seems more appropriate to the situation. I did give you two options.")
                                                    else:
                                                        print("You didn't even enter anything")
    elif decision == "redo" or decision == "back":              # Too early
        print("'" + decision + "' can't do it's intended effect at the start of the program.")
    elif decision == "end":             # Was this not interesting enough?
        exit()
    elif decision == "log in" or decision == "sign in" or decision == "log":        # If there's going to be an account creating, you may as well log in as well
        a = 1
        while a == 1:
            print("Type 'forgot' as your password in case you can't remember it")     # This option's always available, and the only way I can find use of saved emails
            username = input("Username:")           # User enters their email
            if username.lower() == "redo" or username == "back":
                a = 0
                break           # This just ends this specific while loop
            elif username.lower() == "end":
                exit()
            password = input("Password:")       # The password is entered as well
            if password.lower() == "redo" or password.lower() == "back":        # Given that this is close to the start, they both reroute to the beginning
                a = 0
            elif password.lower() == "end":
                exit()
            elif password.lower() == "forgot":
                a = 2
                while a == 2:
                    email = input("Enter your email:")
                    if email.lower() == "redo":
                        a = 0
                    elif email.lower() == "back":
                        a = 1
                    elif email.lower() == "end":
                        exit()
                    elif verify(email):         # Checks if the entered email is correct, and if so, prints the related password
                        a = 1
                    else:
                        print("Invalid email entered")
            else:
                a = 2
                while a == 2:
                    if not confirm(username, password):     # If the duo entered don't sync:
                        print("Invalid details entered")
                        a = 1
                    elif confirm(username, password):
                        player_user, player_pass = username, password
                        player_email = actual(username)     # This just checks the account for their email
                        print("Successfully logged in\nWelcome, " + player_user + "\nYou can't use the 'redo' command anymore")         # Dictionaries are probably more preferred over lists when it comes to account storage
                        a = 3
                        while a == 3:
                            line_delete()       # Best place to use this function, because I know that here, bugs could revolve around empty lines
                            decision = input("Would you like to change your 'email', 'username', 'password':")
                            decision = decision.lower()
                            if decision == "back" or decision == "redo":
                                print("You can't use this command")
                            elif decision == "no" or decision == "false" or decision == "nope" or decision == "nah" or decision == "na" or decision == "exit":
                                print("Goodbye " + player_user)
                                time.sleep(1)
                                exit()
                            elif decision == "email" or decision == "email address" or decision == player_email:
                                a = 4
                                while a == 4:
                                    email = input("Enter your new email:")  # User enters their email
                                    length = len(email)  # Length of the email
                                    index = email.find('@')  # Where the "@" character is placed or if there is one
                                    index2 = email.find(".")  # Where the "." character is placed if there is one
                                    domain = length + 1 - index
                                    if length == 0:
                                        print("You need to enter an email in case you forget your password")
                                    elif email == player_email:
                                        print("This is your current email")
                                    elif email.lower() == "end":
                                        print("Goodbye, " + player_user)
                                        exit()
                                    elif email.lower() == "back":
                                        a = 3
                                    elif email.lower() == "redo":
                                        print("You can't start again at this point")
                                    elif index == 0 or index == -1 or index == length - 1:  # Sees if the "@" symbol is at the start or the end
                                        print("Invalid Email")
                                    elif index2 == 0 or index2 == -1 or index2 == length - 1:  # Sees if the "@" symbol is at the start or the end
                                        print("Invalid Email")
                                    elif index > 63 or domain > 255:  # Checks the length of the local and domain part of the email
                                        print("Invalid Email")
                                    elif not email_allowed(email) or not index_special(email[0], email[length - 1]):  # If false was returned
                                        print("Invalid Email")
                                    elif not double(email):  # Checks if any false was returned for the double function
                                        print("Invalid Email")
                                    elif not duplicate_email(email):  # Checks if the email has already been registered
                                        print(email + " has already been registered")  # Valid, but has already been registered
                                    else:
                                        new_email(email)        # The new email gets saved
                                        rewrite()               # Rewrites the file
                                        print("You've successfully changed your email")     # Doesn't even ask for a confirmation
                                        player_email = email            # Exactly what it says
                                        a = 3                # Returns back to the 3rd stage when asking if anything's needs editing
                            elif decision == "username" or decision == "user" or decision == "user name" or decision == "name":
                                a = 4
                                while a == 4:
                                    username = input("Type specs to view the requirements\nEnter your new username:")  # Person enters their username
                                    length = len(username)  # Length of entered username
                                    if username.lower() == "end":
                                        print("Goodbye, " + player_user)
                                        exit()
                                    elif username.lower() == "specs":
                                        print("Has to be between 5-12 characters\nCan't contain specific special characters")
                                    elif username.lower() == "back":
                                        a = 3
                                    elif username.lower() == "redo":
                                        print("As previously stated, you can't")
                                    elif length == 0:
                                        print("You've got to enter something.'")
                                    elif not special_name(username) and 13 > length > 4:
                                        print("Invalid.Can't contain specific special characters.")
                                    elif special_name(username) == True and 5 > length:
                                        print("Invalid. Has to be at least 5 characters in length.")
                                    elif length > 12 and special_name(username):
                                        print("Invalid. The maximum number of characters a username can contain is 12.")
                                    elif length > 12 or length < 5 and not special_name(username):
                                        print("Invalid. Has to be between 5-12 characters & it can't contain specific special characters.")
                                    elif not duplicate_name(username):
                                        print("Username is too similar")
                                    else:
                                        new_user(username)
                                        rewrite()
                                        print("You've successfully changed your username")
                                        player_user = username
                                        a = 3
                            elif decision == "password" or decision == "password" or decision == "pass word":
                                a = 4
                                while a == 4:
                                    password = input("Enter a valid password:")
                                    word_length = len(password)
                                    hidden_pass = "*" * word_length
                                    errors = []
                                    if password.lower() == "specs":
                                        print("6-128 characters\nAt least one uppercase & lowercase character\nAt least one digit\nOnly alphanumeric characters")
                                    elif word_length == 0:
                                        print("You need a password as a verification.")
                                    elif password.lower() == "end":
                                        print("Goodbye, " + player_user)
                                        exit()
                                    elif password.lower() == "back":
                                        a = 3
                                    elif password.lower() == "redo":
                                        print("This option isn't available anymore")
                                    else:
                                        caps(password)
                                        lower(password)
                                        number(password)
                                        letter()
                                        special(password)
                                        if errors:
                                            for m in range(len(errors)):
                                                print(errors[m])
                                        else:
                                            new_pass(password)
                                            rewrite()
                                            print("You've successfully changed your password")
                                            player_pass = password
                                            a = 3
# Expected 400 lines in total
