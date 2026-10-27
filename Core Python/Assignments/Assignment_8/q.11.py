# WAP to check if a given number is Armstrong number or not. For each task create separate functions.


def armstrong_no():
    n = int(input('Enter the number: '))
    original = n
    digits = len(str(n))
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10
    if original == total:
        print(original, 'is an Armstrong number')
    else:
        print(original, 'is not an Armstrong number')
armstrong_no()
