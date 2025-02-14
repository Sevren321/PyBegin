# Function to reverse a word
def reverse_word(word):
    return word[::-1]

# Input from user
user_input = input("Enter a sentence: ")
 
# Split the sentence into words
words = user_input.split()

# Reverse each word and order of words
reversed_words = [reverse_word(word) for word in reversed(words)]

# Join the reversed words into a single string 
result = ' '.join(reversed_words)

# Print the result
print(result)