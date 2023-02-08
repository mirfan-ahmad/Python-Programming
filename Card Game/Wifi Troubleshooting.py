def wifi_troubleshooting():
    print("Wifi is not connecting with any device??")
    print("Reboot the Computer and try to connect")
    fixed = input("Did that fix the problem Enter yes or no = ")
    if fixed == "yes":
        return
    else:
        print("Reboot the router and try to connect")
        fixed = input("Did that fix the problem Enter yes or no = ")
        if fixed == "yes":
            return
        else:
            print("Make sure the cables between the router & modem are plugged in firmly")
            fixed = input("Did that fix the problem Enter yes or no = ")
            if fixed == "yes":
                return
            else:
                print("Move the router to a new location and try to connect")
                fixed = input("Did that fix the problem Enter yes or no = ")
                if fixed == "yes":
                    return
                else:
                    print("Get a new router")


wifi_troubleshooting()
