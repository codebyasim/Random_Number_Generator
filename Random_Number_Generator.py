import random  # Importing the random module to generate random numbers

# Generating a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)

# Printing the random number and its data type (should be <class 'int'>)
print("Random Number:", random_number)
print("Data Type:", type(random_number))

# Examples of naming conventions for multi-word variables

camelCaseVariable = "ThisIsCamelCase"      # Camel Case → first word lowercase, next words start with uppercase letters
PascalCaseVariable = "ThisIsPascalCase"    # Pascal Case → every word starts with uppercase (also called UpperCamelCase)
snake_case_variable = "this_is_snake_case" # Snake Case → all lowercase with underscores between words (Python preferred style)

# Type conversion examples

float_number = float(random_number)      # Converting integer to float
complex_number = complex(random_number)  # Converting integer to complex number

# Printing converted values and their data types
print("Random Number as Float:", float_number)
print("Data Type after Conversion to Float:", type(float_number))

print("Random Number as Complex:", complex_number)
print("Data Type after Conversion to Complex:", type(complex_number))
