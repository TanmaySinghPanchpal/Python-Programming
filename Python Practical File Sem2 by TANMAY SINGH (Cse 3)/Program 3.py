# Python Program to Demonstrate Operators and Precedence

# Operators and precedence
a,b,c = 3,4,5

# Arithmetic Operators
print("Addition :", a + b,
    "\nSubtraction :", a - b,
    "\nMultiplication :", a * b,
    "\nDivision :", a / b,
    "\nModulus :", a % b,
    "\nExponent :", a ** c)

# Precedence
result = a + b * c - b
# * has higher precedence than + or -
print("Result with Precedence :", result)
