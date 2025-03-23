# Python Program to Find the Average of n Natural Numbers
n = int(input("Enter n: "))
sum_n = n * (n + 1) // 2
average = sum_n / n
print(f"Average of first {n} natural numbers is {average}")
