def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature} degrees Celsius.")
