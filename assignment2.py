
lst = []

# Number of students as input
n = int(input("Enter number of students: "))

# Iterating till the range
for i in range(n):
    ele = str(input(f"Enter student name {i + 1}: "))
    # Adding the name of students
    lst.append(ele)

print("Initial List:", lst)

# Input multiple items to remove, separated by spaces
names_to_remove = input("Enter the name of student to remove (separated by spaces): ").split()

# Convert the input to integers
items_to_remove = [str(item) for item in names_to_remove]

# Using list comprehension to create a new list excluding the items to remove
lst = [ele for ele in lst if ele not in names_to_remove]
print("Updated List:", lst)


def count(text):
    frequency = {char: text.count(char) for char in set(text)}
    return frequency

#text from the user
input = input("Enter the text: ")

# Get the character frequency dictionary
frequency = count(input)
print("Character Frequency:", frequency)


def filter_even_numbers(numbers):
    # Using filter()  to filter even numbers
    even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

# tuple of integers
input_tuple = tuple(map(int, input("Enter integers separated by spaces: ").split()))

#new tuple with even numbers only
result_tuple = filter_even_numbers(input_tuple)
print("Tuple with even numbers:", result_tuple)
