# Python Program to Display Fibonacci Sequence
num = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Sequence:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b
