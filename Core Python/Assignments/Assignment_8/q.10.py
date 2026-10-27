# Write a program to check if entered year is a leap year or not.

def year_leap():
    n = int(input('Enter the year: '))

    if n % 400 == 0:
        print('Leap year')
    elif n % 100 == 0:
        print('Not a leap year')
    elif n % 4 == 0:
        print('Leap year')
    else:
        print('Not a leap year')

year_leap()
