# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.//

basic = int(input("Enter basic salary of employee: "))
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic
total_salary = basic + da + ta + hra

print(f'Total salary of employee is: {total_salary}')