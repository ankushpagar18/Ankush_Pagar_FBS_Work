# Write a program to accept distance in km and convert it into meters and centimeters both.

km = float(input("Enter distance in km: "))

meters = km * 1000
centimeters = km * 100000

print("Meters =", meters)
print("Centimeters =", centimeters)
