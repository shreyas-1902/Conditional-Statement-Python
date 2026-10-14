side1=int(input("Enter first side of triangle:"))
side2=int(input("Enter second side of triangle:"))
side3=int(input("Enter third side of triangle:"))

if(side1==side2 and side1==side3):
    print("Triangle is Equilateral")
elif(side1==side2 or side1==side3 or side2==side3):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")