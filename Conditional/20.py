age=int(input("Enter the age:"))
halfticket=20
fullticket=40

if(age<=12 or (age>=65 and age<75)):
    print("Ticket:",halfticket)
elif(age>12 and age<65):
    print("Ticket:",fullticket)
else:
    print("Free Ticket")