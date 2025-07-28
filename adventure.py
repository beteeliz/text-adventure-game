def intro():
    print("👻 You wake up inside a dusty, locked room in a haunted mansion.")
    print("There's a door to your 'left' and a staircase leading 'down'.")
    choice = input("> ").lower()
    if choice == "left":
        library_room()
    elif choice == "down":
        basement()
    else:
        print("You trip over a chair and knock yourself out. 💀")
        game_over()

def library_room():
    print("📚 You enter an old library filled with cobwebs.")
    print("A ghostly whisper says, 'Read the cursed book or take the golden key.'")
    choice = input("Do you choose 'book' or 'key'? > ").lower()
    if choice == "book":
        print("The book curses you. You become part of the mansion. 💀")
        game_over()
    elif choice == "key":
        print("You grab the key and escape through a hidden door! 🔑")
        win()
    else:
        print("You hesitate too long. The ghost takes your soul.")
        game_over()

def basement():
    print("🔦 You descend into a dark basement. It smells of mold and mystery.")
    print("You hear something moving. Do you 'hide' or 'explore'?")
    choice = input("> ").lower()
    if choice == "hide":
        print("Smart move. The danger passes. You find a ladder and climb out!")
        win()
    elif choice == "explore":
        print("A shadowy figure grabs you. You vanish without a trace. 💀")
        game_over()
    else:
        print("Frozen in fear, you fall into a pit.")
        game_over()

def win():
    print("🎉 You escaped the haunted mansion! You're free!")

def game_over():
    print("💀 Game Over.")
    replay = input("Try again? (yes/no) > ").lower()
    if replay == "yes":
        intro()
    else:
        print("Thanks for playing. Sleep tight... 😈")

intro()