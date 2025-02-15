def is_palindrome(s):
    # Normalize the string by removing non-alphanumeric characters and coverting to lowercase
    normalized = ''.join(char.lower() for char in s if char.isalnum())


    # Compare the normalized string with its revers
    return normalized == normalized[::-1]
    

# Main program
if __name__ == "__main__":
    # Example test cases
    test_strings = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat i saw?", "hello"]

    for string in test_strings:
        if is_palindrome(string):
            print(f"'{string}' is a palindrome.")
        else:
            print(f"'{string}' is not a palindrome.")