def letter(password):       # This is new
    if len(password)>7:
        incorrect.append("")
        return True
    else:
        incorrect.append("Not Long Enough")
        return True

def caps(password):
    i=0         # i = o
    incorrect=incorrect     # Hey reader, incorrect = incorrect. That's all the info you need, no information on what incorrect is actually equal to in the function.
    while i!=count:     # Instead of using count controlled loops, I decide to use conditional controlled loops. Still wrong though
        if password[i].isupper:     # Checks if the first character is uppercase or not
            incorrect.append("")
            # Wondering why I left this empty gap
            i=count     # Given that there is an uppercase char, i becomes equal to count
        else:
            incorrect=incorrect.remove("No Caps")       # I seriously don't understand why I did this, nothing would be removed.
            incorrect.append("No Caps")         # Above line may as well be deleted
            i=i+1       # i becomes 1 number higher
    else:
        return True     # Either way, true is returned


pass1=input("Enter Password:")      # I'm planning on going through the short anime: "Akame Ga Kill". Hope I like it
count=len(pass1)        # count is the same as the length of the password
incorrect=[]            # Empty, square brackets

if letter(pass1)==True:
    num=incorrect[0]        # Ok, so num(which is short for number though I decided to use it as a alphabetical string) is equal to the first string in the list
    incorrect=incorrect.remove(num)     # I then choose to delete num from the list, which means I'm deleting the first string
    if caps(pass1)==True:       # Someone's finished 5/8 animes during this crisis, I consider that impressive, though I hope they are doing other stuff
        capital=incorrect[0]    # It would be ironic though for me to say they should do the school online lessons, not like I've done any worthwhile work related to it
        incorrect=incorrect.remove(capital)     # I did it again except with a different variable, 'capital'
        print(num+capital)      # Oh, I understand why I did it, makes somewhat sense. Still wrong, but understandable.
# "anime" seems to be considered a typo. That's all that's stood out to me that I may remember while commenting ^^^
