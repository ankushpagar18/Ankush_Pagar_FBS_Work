# Write a program find reverse of a number

def rev_no():
    n = int(input('Enter the number: '))
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
res = rev_no()
print(res)


