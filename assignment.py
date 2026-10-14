def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition decide which numbers are passed to add_one.
# Your answer: 3, 4

# 2. What does add_one(2) return? Explain the difference between return inside the function and print in the loop.
# Your answer: add_one(2) returns 3. A return statement passes a computed value back to the exact location in the code 
# where the function was called, allowing the program to use that resulting data in further operations.
# By contrast, print() only displays a visual representation of a value on the console screen for the user to read; it does not output any usable data back to the program's memory.