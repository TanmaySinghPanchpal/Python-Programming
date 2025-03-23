# Python Program to Find the Sum of Digits in a Number
num = int(input("Enter a number: "))
sum_digits = sum(map(int, str(num)))
print(f"Sum of digits of {num} is {sum_digits}")
