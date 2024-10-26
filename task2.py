def count(text):
    frequency = {char: text.count(char) for char in set(text)}
    return frequency

#text from the user
input = input("Enter the text: ")

# Get the character frequency dictionary
frequency = count(input)
print("Character Frequency:", frequency)
