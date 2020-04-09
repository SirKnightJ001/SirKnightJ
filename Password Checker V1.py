def letter(password):           # Function that checks the number of characters in the password
    if len(password)>7:         # If it's over 7 characters
        incorrect.append("")    # An empty space gets added to the list: 'incorrect'
        return True             # Returns that it's true(in this case, it has the necessary number of characters
    else:                       # Translation: else
        incorrect.append("Not Long Enough")     # The text in the brackets gets added to the list
        return True                             # Returns True just because

def mixed(password):            # Function that checks if there are uppercase & lowercase characters
    for i in range(0,count1):               # Rookie mistake, didn't enter what count1 was(probably the length of the password)
        if password[i].isupper():               # Another rookie mistake, this only checks if the first character is uppercase or not, instead of each separately
            for i in range(0,count1):           # Now that I look at this, I'm really disappointed at myself
                if i.islower():                 # I was supposed to use this code as a reflection of my improvement, but it seems to be hours of wasted lines
                    return True                 # Nevertheless, I've improved dramatically, but that's partially because I was horrible as this evidently shows
                else:                           # I don't really want to prevail further, knowing how embarrassing the first 30 lines are
                    incorrect.append("")        # One day, this will be a good laugh
                    incorrect[n]=("No Lowercase Character")     # I'm not formatting this even though I can, I'm just going to leave it as it is.
                    n=n+1                       # On one hand, it was only a few months ago that I typed this garbage
                    return True                 # On the other hand, in a few months, I've managed to skyrocket in python coding
        else:
            incorrect.append("")                # I don't remember why I did this
            incorrect[n]=("No Uppercase Character")     # I...what's 'n' even supposed to be equal to?
            n=n+1           # I probably thought that I could use outer scope variables in functions without using the global command
            for i in range(0,count1):
                if password[i].islower():           # Unintentionally checks if the first character is lowercase
                    return True                     # In my defence, it's not like my class learn how to program in class, all we do is theory
                else:
                    incorrect.append("")
                    incorrect[n]=("No Lowercase Character")     # I wonder how many are actually going to read 1/8 of my comments
                    n=n+1
                    return True         # If it was going to return anything, it may ass well have been false

def num(password):              # Variable that checks the password entered for any numbers
    for i in range(0,count1):       # Again, count1 appears
        if password[i].isdigit():   # Checks if the first, and only first, character is a digit
            return True
        else:
            incorrect.append("")
            incorrect[3]=("No digits")    # Why 3
            n=n+1
            return True

incorrect=[]            # All that's incorrect should be in this list
pass1=input("Enter Password:")      # The user enters their password
count1=len(pass1)                   # Count1 is equal to the length of the password
count1=int(count1)-1                # int turns whatever is in the brackets into a number. Question is, why did I use it, and a second question, why did I create a new line just for a single subtraction?
n=1                         # There we go, I guess I did think I could use a global variable in functions



# Unnecessary number of empty lines


if letter(pass1)==True:             # There was a much simpler way of me typing this
    if mixed(pass1)==True:              # At least it explains why I was always returning True
        if num(pass1)==True:                # Still didn't have to return anything though
            print(incorrect)                    # Print the list of mistakes
            if incorrect[0]=="":                    # If its empty:
                print("Valid Password")                 # Your password is deemed valid and the program ends

# Summary, my first time writing a detailed-ish password code, that would only accept entries that follow a specification. Massive failure, but not a big deal.
