month=int(input("Enter month:"))

match month:
    case 1|3|5|7|8|10|12:
        print("31 days in month")
    case 4|6|9|11:
        print("30 days in month")
    case 2:
        print("28 or 29 days in month")
    case _:
        print("Enter correct month")