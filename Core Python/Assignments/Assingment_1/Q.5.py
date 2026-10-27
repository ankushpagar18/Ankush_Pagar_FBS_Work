# Write a program to enter P, T, R and calculate Compound Interest.

P = 5000
T = 10
R = 2

CI = P * (1 + R / 100) ** T
CI = CI - P
print("Compound interest is  :", CI)
