command = ""
Started = False
stopped =False
while True:
    command = input(">:")
    if command.lower() == "start":
        if Started:
            print("Car has already started!")
        else:
            Started = True
            print("Car started!")
    elif command.lower() == "stop":
        if stopped:
            print("Car has Already stopped")
        else:
            stopped = True
            print("Car Stopped!")
    elif command.lower() == "help":
        print("""
Start: To Start the Game!
Stop:  To Stop the Game!
Quit:  To Quit the Game!
        """)
    elif command.lower() == "quit":
        break
    else:
        print("I don't understand that")



