# WAP to print factorial of a number .
#while loop
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i = i + 1
print("Factorial of", n, "is", factorial)

#for loop
# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i
# print("Factorial of", n, "is", factorial)
