print("Food Menu" "\n" "1.Kaju Paneer" "\n" "2.Paneer Kadai" "\n" "3.Shahi Paneer" "\n" "4.Dal Tadaka")
ch=int(input("Enter your choice:"))

match ch:
    case 1:
        print("You selected Kaju Paneer")
    case 2:
        print("You selected Paneer Kadai")
    case 3:
        print("You selected Shahi Paneer")
    case 4:
        print("You selected Dal Tadaka")
    case _:
        print("Please enter correct choice")