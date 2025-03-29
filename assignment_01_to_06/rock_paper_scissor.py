import random

def play(user_input,comp_input):
    if user_input == comp_input:
        print("Tie !")

    if user_input == "rock" and comp_input == "scissor" or user_input == "paper" and comp_input == "rock" or user_input == "scissor" and comp_input == "paper":
        print("User Won !")
    
    print("User Lost !")

def main():
    options = ["rock","paper","scissor"]
    rand_choice = random.choice(options)
    user_input = input("Type (Rock or Paper or Scissor) : ").strip().lower()

    play(user_input,rand_choice)


if __name__ == "__main__":
    main()