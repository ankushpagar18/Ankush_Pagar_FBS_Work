# Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.

n = int(input("Enter a 3-digit number: "))

first = n // 100
second = (n // 10) % 10
third = n % 10

if first == 2 * second and first * 2 == third:
    print("Yes, you have done it")
else:
    print("Please try next time")
