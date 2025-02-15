import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\"/:;{}|<>]", password):
        strength += 1

    # Check for both upper and lower case letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1

    # Strength evaluation
    if strength == 4:
        return "Very Strong"
    elif strength == 3:
        return "Strong"
    elif strength == 2:
        return "Moderate"
    else:
        return "Weak"
    
password = input("Enter a password: ")
print(f"Password Strength: {check_password_strength(password)}")