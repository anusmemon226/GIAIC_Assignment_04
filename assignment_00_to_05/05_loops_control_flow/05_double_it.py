def main():
    try:
        user_number = int(input("Enter Number to Double till 100 : "))
        while user_number < 100:
            user_number = user_number * 2
            print(user_number,end=" ")
    except ValueError:
        print("Invalid Input")

if __name__ == "__main__":
    main()