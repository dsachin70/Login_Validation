#Login System python program
print("Login System python program")

print(20*"*")
import re
# Predefined password
correct_password = "Pass@123"

# Function to validate password
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?]", password):
        return False
    return True

# User gets 3 attempts
for attempt in range(3):
    print(f"Attempt {attempt + 1} of 3")

    # Initialize user_input
    user_password = ""

    # while loop to keep asking until user provides a valid input
    while True:
        user_password = input("Enter your password : ").strip()

        # check if the user enter a valid
        if user_password:
            if is_valid_password(user_password):
                break
            else:
                print("Password must be at least 8 characters, include one uppercase letter, one number, and one special character.")
        else:
            print("Password cannot be empty. Try again.")

    # check if the password is correct
    if user_password == correct_password:
        print("Access granted ! ")
        break
    else:
        print("Incorrect password.")
else:
    print("Account locked. Too many failsed attempts.")
