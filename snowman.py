import game_logic

def main():
    game_logic.play_game()
    wish_to_continue = True
    while wish_to_continue == True:
        again = input("Do you want to play again? (y/n)")
        if again.lower() == "y":
            print("")
            game_logic.play_game()
        if again.lower() == "n":
            wish_to_continue = False
        elif "y" not in again.lower() and "n" not in again.lower():
            print("invalid input")
            print("")

    print("Goodbye!")

if __name__ == "__main__":
    main()