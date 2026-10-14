print("1.Addition" "\n" "2.Substraction" "\n" "3.Multiplication" "\n" "4.Division")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
cho=int(input("Enter your choice:"))

match cho:
    case 1:
        print("Addition=",num1+num2)
    case 2:
        print("Substraction=",num1-num2)
    case 3:
        print("Multiplication=", num1*num2)
    case 4:
        print("Division=", num1/num2)
    case _:
        print("Enter correct choice...")