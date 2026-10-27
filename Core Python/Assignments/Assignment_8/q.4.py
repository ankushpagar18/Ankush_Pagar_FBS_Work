# Sum of all odd numbers between 1 to n
def sum_odd_no():
    n = int(input('Enter the number:'))
    total = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            total += i
    return total
res = sum_odd_no()
print(res)
        
