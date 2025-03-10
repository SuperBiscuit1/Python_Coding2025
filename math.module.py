# Import the math module
import math

# Ask the user for a number to calculate its square root
number = float(input("Enter a number to find its square root: "))
sqrt_result = math.sqrt(number)
print(f"The square root of {number} is: {sqrt_result}")

# Ask the user for a base and exponent to calculate the power
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is: {power_result}")

# Print the value of pi (π) rounded to 5 decimal places
pi_rounded = round(math.pi, 5)
print(f"The value of π (pi) rounded to 5 decimal places is: {pi_rounded}")
