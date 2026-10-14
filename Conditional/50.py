print("ATM MENU" "\n" "1. Check Balance" "\n" "2. Deposit Money" "\n" "3. Withdraw Money" "\n" "4. Exit")

cho = int(input("Enter your choice: "))

match cho:
    case 1:
        print("Your balance is ₹5000")
    case 2:
        amount = int(input("Enter deposit amount: "))
        print("Amount deposited:", amount)
    case 3:
        amount = int(input("Enter withdrawal amount: "))
        print("Amount withdrawn:", amount)
    case 4:
        print("Thank you for using our ATM...")
    case _:
        print("Invalid choice")