def longest(strings):
    if not strings:
        return None  # Return None for an empty list

    # Initialize with the first string in the list
    longest_str = strings[0]

    # Iterate through the list to find the longest string
    for s in strings:
        if len(s) > len(longest_str):
            longest_str = s

    return longest_str

# Example usage
input_strings = ["apple", "banana", "kiwi", "orange", "pear"]
result = longest(input_strings)

print(f"The longest string is: {result}")
