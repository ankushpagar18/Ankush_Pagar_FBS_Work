##sum of series
def sum_of_series():
    n = int(input("Enter the no :"))
    total = 0
    for i in range(1,n+1):
        total+=i
    return total
res = sum_of_series()
print(res)


###sum of  fact
def sum_of_factorial():
    n = int(input("Enter the no: "))
    total = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact = fact * j
        total = total + fact
    return total

res = sum_of_factorial()
print(res)

##sum of power series
def sum_of_power():
    n = int(input("Enter the no: "))
    total = 0
    for i in range(1,n+1):
        total += i ** i
    return total
res = sum_of_power()
print(res)   #ex. n = 1¹ + 2² + 3³ + ... + nⁿ

