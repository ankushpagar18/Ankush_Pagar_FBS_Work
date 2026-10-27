# Write a program to input angles of a triangle and check whether triangle is valid or not.

a = float(input("Enter the 1st angle :"))
b = float(input("Enter the 2nd angle :"))
c = float(input("Enter the 3rd angle :"))
sum = (a + b + c)
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("vaild triangle")
else:
    print("Invaild triangle")

