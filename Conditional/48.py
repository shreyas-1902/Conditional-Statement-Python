print("Language Menu" "\n" "1.Python" "\n" "2.Java" "\n" "3.React" "\n" "4.JavaScript")


cho = int(input("Enter your language choice: "))

match cho:
    case 1:
        print("You selected Python")
    case 2:
        print("You selected Java")
    case 3:
        print("You selected React")
    case 4:
        print("You selected JavaScript")
    case _:
        print("Invalid choice")