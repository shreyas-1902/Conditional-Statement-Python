marks=int(input("Enter student marks:"))
atten=int(input("Enter student attendance:"))

if(marks>50 and atten > 75):
    print("Student is eligible for exam...")
else:
    print("Student is not eligible for exam...")