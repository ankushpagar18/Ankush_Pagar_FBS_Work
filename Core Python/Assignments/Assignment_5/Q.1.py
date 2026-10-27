# Write a program to prompt user to enter userid and password. If Id and
userid = input("Enter your user ID: ")
password = input("Enter your password: ")
for i in range(2):
    if userid == "ankush01" and password == "010101":
        print("Login successful!")
        break
    else:
        print("Invalid user ID or password. Please try again.")
        userid = input("Enter your user ID: ")
        password = input("Enter your password: ")
if userid == "ankush01" and password == "010101":
    print("Login successful!")
else:
    print("You have used all attempts. Please try again later.")
