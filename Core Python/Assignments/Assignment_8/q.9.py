# Write a program to check if entered number is a palindrome or not.

def palindrome_no():
    n = int(input('enter the no.'))
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if original == rev:
        print(original,'no. is pallindrome no')
    else:
        print(original,'no.is not pallindrome no')
        
palindrome_no()
