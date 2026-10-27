# Write a program to calculate profit or loss.

cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))
if sp > cp :
    profit = sp - cp
    print("Profit: ", profit)
elif sp <cp :
    loss = cp - sp
    print("Loss: ", loss)
else:
    print("koi baat nahi")