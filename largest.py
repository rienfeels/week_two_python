def largest(numbers):
    if not numbers:
        return None  # Return None for an empty list

    # Initialize with the first number in the list
    largest_num = numbers[0]

    # Iterate through the list to find the largest number
    for num in numbers:
        if num > largest_num:
            largest_num = num

    return largest_num

# Example usage
input_numbers = [11, 20, 42, 97, 23, 10]
result = largest(input_numbers)

print(f"The largest number is: {result}")
