def make_change(total_charge, payment):
    # Find the difference
    difference = round(payment - total_charge, 2)
    # Split the difference into bills and coins
    # Convert the difference into a string
    difference_as_string = str(difference)
    # Split the string into parts
    parts = difference_as_string.split('.')
    # Define the bills and coins based on the parts
    bills = parts[0]
    # Note to make the coins go to two decimal places
    coins = parts[1]
    return count_bills(bills), count_coins(coins)


def count_bills(payment_in_bills):
    payment_in_bills = int(payment_in_bills)
    hundreds = payment_in_bills // 100
    payment_in_bills %= 100
    fifties = payment_in_bills // 50
    payment_in_bills %= 50
    twenties = payment_in_bills // 20
    payment_in_bills %= 20
    tens = payment_in_bills // 10
    payment_in_bills %= 10
    fives = payment_in_bills // 5
    payment_in_bills %= 5
    singles = payment_in_bills // 1
    return (singles, fives, tens, twenties, fifties, hundreds)


def count_coins(payment_in_coins):
    payment_in_coins = int(payment_in_coins)
    quarters = payment_in_coins // 25
    payment_in_coins %= 25
    dimes = payment_in_coins // 10
    payment_in_coins %= 10
    nickels = payment_in_coins // 5
    payment_in_coins %= 5
    pennies = payment_in_coins // 1
    return (pennies, nickels, dimes, quarters)


print(make_change(148.49, 200))
