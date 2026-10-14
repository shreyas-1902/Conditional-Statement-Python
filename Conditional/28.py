amt=int(input("Enter shopping amount:"))

if(amt<0):
    print("Enter correct amount...")
elif(0>= amt >= 1000):
    dis=amt*5/100
    amt=amt-dis
    print("Discounted amount is:", amt)
elif(1001>= amt >= 10000):
    dis=amt*10/100
    amt=amt-dis
    print("Discounted amount is:", amt)
elif(10001>= amt >= 10000):
    dis=amt*15/100
    amt=amt-dis
    print("Discounted amount is:", amt)
else:
    dis=amt*20/100
    amt=amt-dis
    print("Discounted amount is:", amt)