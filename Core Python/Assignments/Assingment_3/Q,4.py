# Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = float(input("Enter first angle :"))
b = float(input("Enter second angle :"))
c = float(input("Enter third angle :"))
if a + b > c and a + c > b and b + c > a:
    print("Vaild angle.")
else:
    print("Invaild angle.")