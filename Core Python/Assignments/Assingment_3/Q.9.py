# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
maths = float(input("Enter marks of subject maths: "))
physics = float(input("Enter marks of subject physics: "))
chemistry = float(input("Enter marks of subject chemistry: "))
hindi = float(input("Enter marks of subject hindi: "))
marathi = float(input("Enter marks of subject marathi: "))

total = (maths + physics + chemistry + hindi + marathi)
percentage = total / 5

print("total = ", total)
print("percentage = ", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Pass")
else:
    print("Fail")
