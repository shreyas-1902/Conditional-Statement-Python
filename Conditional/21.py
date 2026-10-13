num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if(num1<num2 and num1<num3):
    print("The first number is smallest amongst 3 numbers...")
elif(num2<num1 and num2<num3):
    print("The second number is smallest amongst 3 numbers...")
else:
    print("The third number is smallest amongst 3 numbers...")