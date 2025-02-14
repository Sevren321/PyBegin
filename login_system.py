# Define the correct credentials
correct_username = "admin"
correct_password = "1234"

# Prompt for user input
username = input("Enter username: ")
password = input("Enter password: ")

# Check if the entered credentials match the correct ones
if username == correct_username and password == correct_password:
    print("Logged in successfully!")
else: 
    print("Login failed")