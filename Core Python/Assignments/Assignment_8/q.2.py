# Write a program to calculate area of circle
def areaOfcircle():
    r = int(input('Enter the radius of circle :'))
    area = 3.14 * r ** 2
    return area
res = areaOfcircle()
print(res)