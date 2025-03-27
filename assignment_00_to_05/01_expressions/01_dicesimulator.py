import random as rand
def rollDice():
    dice1 = rand.randint(1,6)
    dice2 = rand.randint(1,6)
    total = dice1 + dice2
    print(f"Dice_01 {dice1} - Dice_02 {dice2} - Total of two dice {total}")

def main():
    rollDice()
    rollDice()
    rollDice()
if __name__ == "__main__":
    main()