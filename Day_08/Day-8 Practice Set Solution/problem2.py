# F = (C × 9/5) + 32

Celsius = int(input('Enter the Celsius temperature: '))  # Input for the Celsius temperature

def f_to_c(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32  # Conversion formula from Celsius to Fahrenheit
    return Fahrenheit

print("Temperature in Fahrenheit is:", round(f_to_c(Celsius)))  # Output the converted temperature in Fahrenheit, rounded
