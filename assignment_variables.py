# So the inital assigning of the variable
bandcamp = 45
print("Initial integer value:", bandcamp)

# the reassigning of the same variable
bandcamp = 202.2
print("Reassigned floating-point value:", bandcamp)

#Now converting a string containing a number into an integer and perform arithmetic
thestring = "69"
print("String before conversion:", thestring)

# now to convert the string to an integer
thestring = int(thestring)
print("String after conversion to an integer:", thestring)

# Now to perform arithmetic with the converted integer
result = thestring * 12
print("Result of arithmetic (integer * 5):", result)

# Step 4: Print all values before and after type conversion

print("Initial integer value:", 45)
print("Reassigned floating-point value:", 202.2)
print("String before conversion:", "69")
print("String after conversion to integer:", 12)
print("Result of arithmetic (integer * 12):", 12)