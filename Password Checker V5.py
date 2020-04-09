import re       # This is what I currently use to check for special characters. You wouldn't believe how many days I spent trying to effectively check if a string has any
# In this version though, I didn't even use the module correctly, therefore a logic error that I didn't even realize.
pass1 = input("Enter Password that contains:\n8 characters or more\nAt least one uppercase & lowercase character\nAt "
              "least one digit\nNo special characters:")
word_length = len(pass1)
error_check = {}
hidden_pass = "*" * word_length


#   External file, typing username & password at the same time when confirming with a space between, getting rid of the
#   username checker to make it more realistic
#   Every false increases count so I can use count to print problems

def letter(password):
    error_check.update(word_length="")
    if word_length > 7:
        error_check.pop("word_length")
        return True
    else:
        error_check.update(word_length="Not Long Enough")
        return False


def caps(password):
    i = 0
    error_check.update(caps="")
    while i != word_length:
        if password[i].isupper():
            i = word_length
            error_check.pop("caps")
        else:
            i = i + 1
            error_check.update(caps="No Uppercase Character")
    else:
        return True


def lower(password):
    i = 0
    error_check.update(lower="")
    while i != word_length:
        if password[i].islower():
            i = word_length
            error_check.pop("lower")
        else:
            i = i + 1
            error_check.update(lower="No Lowercase Character")
    else:
        return True


def digit(password):
    i = 0
    global word_length
    error_check.update(digit="")
    while i != word_length:
        if password[i].isdigit():
            i = word_length
            error_check.pop("digit")
        else:
            i = i + 1
            error_check.update(digit="No Numerical Character")
    else:
        return True


def special(password):
    error_check.update(special="")
    if re.findall('[A-Za-z0-9]', password):     # findall shouldn't be used as a special character search, my mistake. When I found out(day after school's closure), I was so annoyed. All that time, searching, reading for days for one simple fnction, was wasted
        error_check.pop("special")      # Worst part is that I remember being ecstatic when I thought I figured it out
        return True
    else:
        error_check.update(special="Contains Special Characters")
        return False


letter(pass1)
caps(pass1)
lower(pass1)
digit(pass1)
special(pass1)          # This seems just to be an edit of the special funcion

if not error_check:
    print(f"Your password[{hidden_pass}]is valid.")     # Slightly changed, not that it matters though
else:
    print(error_check.values())
