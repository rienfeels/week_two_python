def shortest(strings):
    if not strings:
        return None  # Return None for an empty list

    # Initialize with the first string in the list
    shortest_str = strings[0]

    # Iterate through the list to find the shortest string
    for s in strings:
        if len(s) < len(shortest_str):
            shortest_str = s

    return shortest_str

# Example usage
input_strings = ["apple", "banana", "kiwi", "orange", "pear"]
result = shortest(input_strings)

print(f"The shortest string is: {result}")
