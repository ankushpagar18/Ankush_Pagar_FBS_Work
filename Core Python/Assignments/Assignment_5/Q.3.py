# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them 
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
passengers = int(input("Enter the no. of passengers: "))
ticket_cost = float(input("Enter the cost of ticket: "))
  
total = 0

for i in range(passengers):

    age = int(input("Enter the age: "))

    if age < 12:
        amount = ticket_cost - (ticket_cost * 30 / 100)

    elif age > 59:
        amount = ticket_cost - (ticket_cost * 50 / 100)

    else:
        amount = ticket_cost

    total = total + amount

print("Total ticket amount:", total)


