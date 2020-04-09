def letter(password):
    error_check.update(length="")       # I changed from lists to dictionaries
    if length>7:
           error_check.pop("length")        # Simply put, pop deletes
           return True
    else:
        error_check.update(length="Not Long Enough")        # This was probably right after I learned it in detail
        return False

def caps(password):         # This code has an uppercase and lowercase function, separated for the best
    i=0
    length=len(pass1)
    error_check.update(caps="")     # Update adds whatever's in the brackets or changes
    while i!=length:
        if password[i].isupper():
            i=length
            error_check.pop("caps")     # Nothing wrong so far
        else:
            error_check.update(caps="No Uppercase Character")   # Given that there hasn't been anything wrong for the first 19 lines, unlike the previous attemps, I just ran the code.
    else:
        return True         # I didn't get an error, it did ask me for my password and printed out what it was supposed to

def lower(password):        # That being said, this was the first version that runs, but doesn't work
    i=0
    length=len(pass1)
    error_check.update(lower="")
    while i!=length:
        if password[i].islower():
            i=length
            error_check.pop("lower")
        else:
            error_check.update(lower="No Lowercase Character")
    else:
        return True

def digit(password):
    i=0
    length=len(pass1)
    error_check.update(digit="")
    while i!=length:
        if password[i].isdigit():
            i=length
            error_check.pop("digit")
        else:
            error_check.update(digit="No Numerical Character")   
    else:
        return True
# I'm glad the first 47 lines seem to be valid, even though I'd never refer back to them

def special(password):      # This is also the first version in which I check if there are special characters in the password(what a massive mess this was)
    error_check.update(special="")      # Before I learned about the regex module, this was undoubtedly, the most infuriating puzzle to solve.
    if "<" in password or ","in password or ">" in password or "." in password or "/"in password or "\\"in password or "?" in password or ":" in password or ";" in password or "'" in password or "@" in password or "~" in password or "#" in password or "[" in password or "{" in password or "}" in password or "]" in password or "-" in password or "_" in password or "+" in password or "=" in password or "¬" in password or "`" in password or "|" in password or "!" in password or "\"" in password or "£" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or ")" in password: 
        error_check.update(special="Contains Special Characters")       # ^ At first I decided to do this since, even though unicode is a thing, and it's so long it exceeds my set line length
        return False            # That being said, it doesn't account for every special character, so it's wrong, and I knew it, but worked with it anyway.
    else:
        error_check.pop("special")
        return True
    

pass1=input("Enter Password that contains:\n8 characters or more\nAt least one uppercase & lowercase character\nAt least one digit\nNo special characters:")    # '\n' = newline. As in the following text is shown in a new line
error_check={}
length=len(pass1)
hidden_pass="*"*length      # If your password was "password", your hidden password: "********". Same length basically

letter(pass1)           # This is what I could've done
caps(pass1)             # I didn't need to type any of the return lines
lower(pass1)            # I wonder how many comments I'm going to type in total
digit(pass1)            # White text is a comment
special(pass1)          # 5 functions, just like my complete password checker

if error_check=={}:     # If your error_check dictionary is empty:
    print(f"Your password,{hidden_pass},is valid.")     # I was just trying something I just learned, I don't do this "format code" anymore, if that's even what it's called.
else:       # Largest gap between the other versions so far, in the right direction
    print(error_check.values())     # If it's not empty, prints out all the errors that are within it
