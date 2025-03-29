import random
TOTAL_ROUNDS = 5
current_round = 1
user_score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

while current_round <= 5 :
    user_number = random.randint(1,100)
    comp_number = random.randint(1,100)
   
    print(f"Round {current_round}")
    print(f"Your Number is {user_number}")
    user_input = input("Do you think your number is higher or lower than the computer's ? : ").strip().lower()

    if user_input == "higher" and user_number > comp_number:
        print(f"You were right! The computer's number was {comp_number}")
        user_score += 1
        print(f"Your score is now {user_score}")
    elif user_input == "lower" and user_number < comp_number:
        print(f"You were right! The computer's number was {comp_number}")
        user_score += 1
        print(f"Your score is now {user_score}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {comp_number}")
        print(f"Your score is now {user_score}")
    current_round += 1
    print()

if user_score == TOTAL_ROUNDS:
    print("Wow! You played perfectly!")
elif user_score > int(TOTAL_ROUNDS/2) and user_score < TOTAL_ROUNDS:
    print("You Played Well!")
else:
    print("Better luck next time!")

print("Thanks for Playing")