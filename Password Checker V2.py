incorrect=[]        # Yep, this is the start of version 2
pass1=input("Enter Password:")      # Enter your password
count1=len(pass1)       # Obviously copied from the first version
count1=int(count1)-1    # Didn't even resolve this by doing: count1 = len(pass1) - 1. All in a single line
n=1     # 'n' stands for number in this case, if anyone wonders why I chose that letter to be my integer variable

def letter(password):       # I don't think I have to explain this again
    if len(password)>7:
        incorrect.append("")
        return True
    else:
        incorrect.append("Not Long Enough")
        return True

def caps(password):             # This version seems incomplete. It's so short that I don't even have to scroll down
    for i in range(0,count1):       # This function btw was supposed to check the string for uppercase characters
        if password[i].isuppper():  # But, as before, it only checks the first
            return True     # Returns True if the first is uppercase
        else:
            return False   # I decided to use False returns it seems(or maybe it's a mistake, since I don't use it in the other function when the password is under 7 characters)


if letter(pass1)==True:     # All my characters are squeezed together
    if caps(pass1)==True:       # The further down I go, the greater I woe
        while incorrect is "No Uppercase Character":
            incorrect.remove[n]         # I think I just stopped after seeing my time being wasted, maybe I was tired, or I just needed to take a break from failure for the day.
        
    else:
        incorrect.append("")
        incorrect[n]=("No Uppercase Character")
        n=n+1
# So this is V2, I was extremely harsh when judging V1, I actually appreciate it a lot more now. One of those times that you realize there's always going to be worse
