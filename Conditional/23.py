last=int(input("Enter last reading:"))
current=int(input("Enter current reading:"))

units=current-last
print("Units used:",units)

if(units<0):
    print("Enter correct readings...")
elif(0<= units <=100):
    bill=units*4
    print("Bill:", bill)
elif(101<= units <=400):
    bill=units*7
    print("Bill:", bill)
else:
    bill=units*11
    print("Bill:", bill)
