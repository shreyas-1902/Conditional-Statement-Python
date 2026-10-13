salary=int(input("Enter salary:"))
service=int(input("Enter service years:"))

if(service>=5 and service<=10):
    bonus=salary*10/100
    print("Bonus:",bonus)
elif(service>10):
    bonus=salary*15/100
    print("Bonus:",bonus)
else:
    print("No bonus")