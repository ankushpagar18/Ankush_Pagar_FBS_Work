# Write a program to reverse three-digit number.
number = int(input("Enter a three-digit number: "))
last_digit = number % 10
middle_digit = (number // 10) % 10
first_digit = number // 100
reversed_number = (last_digit * 100) + (middle_digit * 10) + first_digit
print(f"The reversed number of {number} is: {reversed_number}")