def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return not is_even(number)

def only_odds(numbers):
    return [num for num in numbers if is_odd(num)]

# Example usage
input_numbers = [11, 20, 42, 97, 23, 10]
result = only_odds(input_numbers)

print(f"The list of only odd numbers is: {result}")
