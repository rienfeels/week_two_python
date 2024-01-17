def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius_temperature = float(input("Enter temperature in Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")
