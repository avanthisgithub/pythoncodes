#car game
i = 1
while i <= i:
    i = i + 1
    command = str(input(">"))
    if command.lower() == 'help':
        print("start - to start the car")
        print("stop - to stop thw car")
        print("quit - to exit")
    elif command.lower() == 'quit':
        break
    elif command.lower() == 'start':
        print("Car started... Ready to go!")
    elif command.lower() == 'stop':
        print("Car stopped.")
    elif command != 'quit' or 'start' or 'stop' or 'help':
        print("I don't understand that...")










