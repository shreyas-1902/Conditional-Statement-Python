role = input("Enter user role: ").lower()

match role:
    case "admin":
        print("Admin has full access")
    case "user":
        print("User has normal access")
    case "guest":
        print("Guest has limited access")
    case _:
        print("Invalid role")