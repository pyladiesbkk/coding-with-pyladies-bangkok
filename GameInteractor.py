def quitGame():
    print("🔴 Quit the game and go back to main page.")

def goTo(direction):
    print(f"👣  Walking {direction}...")

def save(item):
    print(f"💾 You got {item} 1 ea")


# def interact(action):
#     command = action.split()[0]
#
#     if command == "walking":
#         direction = action.split()[1]
#         goTo(direction)
#
#     elif command == "pickup":
#         item = action.split()[1]
#         save(item)
#
#     elif command == "quit":
#         quitGame()
#
#     else:
#         print("😵 Don't know this command")

def interact(action):
    match action.split():
        case ["walking", direction]:
            goTo(direction)
        case ["pickup", item]:
            save(item)
        case ["quit"]:
            quitGame()
        case _:
            print("😵 Don't know this command")



interact("walking up")
interact("walking down")
interact("walking left")
interact("walking right")

interact("pickup pencil")
interact("pickup wand")

interact("quit")

interact("turnaround")
