age=int(input("Enter your age:"))
weight=int(input("Enter your weight:"))

if(weight>50 and (18<=age<=65)):
    print("You are eligible for voting...")
else:
    print("Your are not eligible for voting...")