import re
# When I decided to expand my password checker, to a {registration & log in} script, I chose to create a separate email & username checker & place them together at the end
# This was very brief, I wasn't trying, so I didn't get much done
def special(email_address):
    if not re.search("[^A-Za-z0-9@.]", email_address):      # Now I'm using the search function to check for special characters. It's like the challenging maths problem, except you can use the web
        return True            # At least I know now, I won't ever go through this experience again
    else:
        return False


def necessary(email_address):       # This function checks the entered email for specific characters that should be in every email
    if "@" in email_address:
        return True
    else:
        return False


x = 0       # Random variable

while x == 0:
    email = input("Enter a valid email address:")
    length = len(email)
    if not special(email) or length < 3 or not necessary:       # If either false is returned:
        print("Invalid Email Address")      # Invalid
    else:
        print("Valid Email Address")        # Valid
        x = 1           # If it's valid, stops looping
