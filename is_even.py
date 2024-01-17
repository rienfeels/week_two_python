def is_even(number):
    return number % 2 == 0

# Example usage
user_number = int(input("Enter a number: "))
result = is_even(user_number)

if result:
    print(f"{user_number} is even.")
else:
    print(f"{user_number} is not even.")
