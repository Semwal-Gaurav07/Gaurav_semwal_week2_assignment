def filter_even_numbers(numbers):
    # Using filter()  to filter even numbers
    even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

# tuple of integers
input_tuple = tuple(map(int, input("Enter integers separated by spaces: ").split()))

#new tuple with even numbers only
result_tuple = filter_even_numbers(input_tuple)
print("Tuple with even numbers:", result_tuple)