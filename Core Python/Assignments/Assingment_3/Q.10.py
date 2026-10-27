# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter gender: ")
age = int(input("Enter age: "))

if gender.lower() == "boys" and age >= 21:
    print("boys are eligible for marriage")
elif gender.lower() == "girls" and age >= 18:
    print("girls are eligible for marriage")
else:
    print("pehle padhai karo fir shadi karo")