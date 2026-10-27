# WAP to calculate area of triangle and rectangle

base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
area_triangle = 0.5 * base * height

length =  int(input("Enter the length of rectangle : "))
breadth = int(input("Enter the breadth of rectangle : "))
area_rectangle = length * breadth
print(f'Area of triangle is : {area_triangle}')
print(f'Area of rectangle is : {area_rectangle}')