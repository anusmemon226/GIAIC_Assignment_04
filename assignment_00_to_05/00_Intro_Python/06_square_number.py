def main():
    try:
        num = float(input("Type a number to see its square: "))
        print(num , " squared is " , num**2)
    except ValueError:
        print("Invalid Input")
if __name__ == '__main__':
    main()