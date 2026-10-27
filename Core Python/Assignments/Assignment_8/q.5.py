# Sum of all prime numbers between 1 to n
def sum_of_prime():
    n = int(input("Enter the number: "))
    total = 0
    for i in range(2, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            total += i
    return total
res = sum_of_prime()
print(res)