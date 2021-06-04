command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("Car is already Started!")
        else:
            car_started = True
            print("Car Started...")
    elif command == "stop":
        if not car_started:
            print("Car is already Stopped!")
        else:
            car_started = False
            print("Car Stopped.")
    elif command == "help":
        print(
            """
start - to start the car
start - to start the car
quit - to quit
        """
        )
    elif command == "quit":
        break
    else:
        print("Sorry! I don't understand that!")
