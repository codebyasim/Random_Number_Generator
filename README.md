# Random Number Generator & Type Conversion Demo

This simple Python script demonstrates:

- How to generate a random number between **1 and 100**.
- How to check the **data type** of variables.
- Examples of **naming conventions** in Python (`camelCase`, `PascalCase`, `snake_case`).
- How to perform **type conversions**: integer → float, and integer → complex.

---

## Features

1. **Random Number Generation**
   - Uses the `random` module (`random.randint(1, 100)`) to generate a number.
   - Prints the number and its data type (`int`).

2. **Naming Conventions**
   - `camelCaseVariable = "ThisIsCamelCase"`
   - `PascalCaseVariable = "ThisIsPascalCase"`
   - `snake_case_variable = "this_is_snake_case"`

3. **Type Conversion**
   - Converts the random integer into:
     - `float` (e.g., `42` → `42.0`)
     - `complex` (e.g., `42` → `42+0j`)
   - Prints both the converted values and their data types.

---

## Example Output

```bash
Random Number: 42
Data Type: <class 'int'>
Random Number as Float: 42.0
Data Type after Conversion to Float: <class 'float'>
Random Number as Complex: (42+0j)
Data Type after Conversion to Complex: <class 'complex'>
