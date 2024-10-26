
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
