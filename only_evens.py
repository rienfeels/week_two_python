def is_even(number):
    return number % 2 == 0

def only_evens(numbers):
    return [num for num in numbers if is_even(num)]

# Example usage
input_numbers = [11, 20, 42, 97, 23, 10]
result = only_evens(input_numbers)

print(f"The list of only even numbers is: {result}")
