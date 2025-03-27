def main():
    try:
        num1 = int(input("Enter Number 01 : "))
        num2 = int(input("Enter Number 02 : "))
        sum = num1 + num2
        print(f"Sum of {num1} and {num2} is : {sum}")
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()