def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return not is_even(number)

# Example usage
user_number = int(input("Enter a number: "))
result = is_odd(user_number)

if result:
    print(f"{user_number} is odd.")
else:
    print(f"{user_number} is not odd.")


#The is_odd function simply calls the is_even function and negates its result using not. 
#This way, it returns True if the number is odd and False if it's not odd.