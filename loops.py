start_number = int(input("Enter the starting number: "))

end_number = int(input("Enter the ending number: "))

print("Incrementing by 1:")
while start_number <= end_number:
    print(start_number, end=" ")
    start_number += 1

step = int(input("\nEnter the step size for incrementing (e.g., 2): "))
print(f"incrementing by {step}:")
while start_number <= end_number:
    print(start_number, end=" ")
    start_number += step

valid_range = range(1, 11)
user_choice = int(input(f"\nEnter a number from {valid_range.start} to {valid_range.stop -1}: "))

if user_choice in valid_range:
    print(f"You chose {user_choice}.")
else:
    print("Your choice is outside the valid range.")

