# WAP to print sum of series upto n.

n = int(input("Enter n: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i = i + 1

print("Sum =", sum)

#for loop
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print("Sum of series upto", n, "is", sum)
