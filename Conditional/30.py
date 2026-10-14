num=int(input("Enter a number:"))

if(-10< num <10):
    print("Number is single digit...")
elif(-100< num <100):
    print("Number is double digit...")
elif(-1000< num < 1000):
    print("Number is triple digit...")
else:
    print("Number is bigger than triple digit...")