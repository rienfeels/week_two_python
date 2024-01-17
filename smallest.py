def smallest(numbers):
    if not numbers:
        return None  # Return None for an empty list

    # Initialize with the first number in the list
    smallest_num = numbers[0]

    # Iterate through the list to find the smallest number
    for num in numbers:
        if num < smallest_num:
            smallest_num = num

    return smallest_num

# Example usage
input_numbers = [11, 20, 42, 97, 23, 10]
result = smallest(input_numbers)

print(f"The smallest number is: {result}")
