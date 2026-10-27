# WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter cost price of book: "))
discount = int(input("Enter discount percentage: "))
selling_price = cost_price - (cost_price * discount / 100)

print(f'Selling price of the book is: {selling_price}')