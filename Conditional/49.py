print("Result Status" "\n" "1.Pass" "\n" "2.Fail" "3.ATKT")

res = int(input("Enter result status: "))

match res:
    case 1:
        print("Student has passed")
    case 2:
        print("Student has failed")
    case 3:
        print("Student has ATKT")
    case _:
        print("Invalid result status")