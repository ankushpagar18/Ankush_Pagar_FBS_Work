# WAP to check if given number Strong Number.

n = int(input("Enter a number: "))
original = n
sum = 0
for i in range(1, n + 1):
    digit = n % 10
    fact = 1
    for j in range(1, digit + 1):
        fact *= j
    sum += fact
    n //= 10
if sum == original:
    print(f"{original} is a Strong Number.")
else:
    print(f"{original} is not a Strong Number.")

    