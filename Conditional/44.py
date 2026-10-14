sig=input("Enter traffic signal colour:").lower()

match sig:
    case "red":
        print("STOP")
    case "yellow":
        print("WAIT")
    case "green":
        print("GO")
    case _:
        print("Invalid colour")