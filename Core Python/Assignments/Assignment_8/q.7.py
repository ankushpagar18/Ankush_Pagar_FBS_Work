# Write a program to find sum of digits of a number.

def sum_digit():
    n = int(input('Enter the number: '))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total
res = sum_digit()
print(res)

