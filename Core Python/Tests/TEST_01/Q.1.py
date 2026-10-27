# Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:


length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area = length * breadth + 0.5 * 3.14 * radius * radius
perimeter = 2 * length + breadth + 3.14 * radius

print("Area =", area)
print("Perimeter =", perimeter)
