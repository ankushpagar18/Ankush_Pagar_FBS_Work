# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))

if num < 100 or num > 999:
    print("Please enter a 3 digit number")
else:
    original = num

    last = num % 10
    num = num // 10

    middle = num % 10
    num = num // 10

    first = num

    reverse = last * 100 + middle * 10 + first

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")