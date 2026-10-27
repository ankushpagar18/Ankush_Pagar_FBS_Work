# Write a program to check if given number is Armstrong number or not. (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

number = int(input("Enter a number: "))
sum_of_powers = 0
num_digits = len(str(number))
for digit in str(number):
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == number:
    print(f"{number} is an Armstrong Number.")
else:
    print(f"{number} is not an Armstrong Number.")