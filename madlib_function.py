def madlib(name="Someone", subject="something"):
    return f"{name}'s favorite subject is {subject}."

# Take user input for name and subject
user_name = input("Enter a name (press Enter to use the default): ").strip()
user_subject = input("Enter a subject (press Enter to use the default): ").strip()

# Call the madlib function with user input or defaults
result = madlib(user_name or None, user_subject or None)

# Print the result
print(result)

