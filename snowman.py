import game_logic

def main():
    wish_to_continue = True
    while wish_to_continue == True:
        game_logic.play_game()
        print("")
        again = input("Do you want to play again? (y/n)")
        if again.lower() == "n":
            wish_to_continue = False
    print("Goodbye!")

if __name__ == "__main__":
    main()