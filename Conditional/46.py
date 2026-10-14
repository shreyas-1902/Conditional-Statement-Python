grade = input("Enter your grade: ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Improvement needed")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")