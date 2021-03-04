rsp = ["가위", "바위", "보"]
Man1 = str(input())
Man2 = str(input())
if(Man1 == rsp[0]):
    if(Man2 == rsp[0]):
        print("Result : Draw")
    elif(Man2 == rsp[1]):
        print("Result : Man2 Win!")
    elif(Man2 == rsp[2]):
        print("Result : Man1 Win!")
    else:
        print("Replay")
elif(Man1 == rsp[1]):
    if(Man2 == rsp[0]):
        print("Result : Man1 Win!")
    elif(Man2 == rsp[1]):
        print("Result : Draw")
    elif(Man2 == rsp[2]):
        print("Result : Man2 Win!")
    else:
        print("Replay")
elif(Man1 == rsp[2]):
    if(Man2 == rsp[0]):
        print("Result : Man2 Win!")
    elif(Man2 == rsp[1]):
        print("Result : Man1 Win!")
    elif(Man2 == rsp[2]):
        print("Result : Draw")
    else:
        print("Replay")
else:
        print("Replay")