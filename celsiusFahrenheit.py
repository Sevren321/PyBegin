# Function to convert Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

# Main program 
print("Celsius to Fahrenheit Converter")
celsius = float(input("Enter a temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsiusToFahrenheit(celsius)

# Output the result
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")