def make_change(total_charge, payment):
    # Validate that payment is greater than or equal to total_charge
    if payment < total_charge:
        return "Error: Insufficient payment"

    # Define the available bill and coin denominations
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]

    # Calculate the change
    change = payment - total_charge

    # Initialize a dictionary to store the count of each denomination
    change_dict = {}

    # Iterate through denominations to calculate the count for each
    for denom in denominations:
        count = int(change // denom)
        change_dict[denom] = count
        change -= count * denom

    # Convert the dictionary to a 2-dimensional tuple
    change_tuple = tuple((denom, count) for denom, count in change_dict.items())

    return change_tuple

# Example usage
total_charge = float(input("Enter the total charge: "))
payment = float(input("Enter the payment: "))

change_result = make_change(total_charge, payment)
print(f"Change: {change_result}")
