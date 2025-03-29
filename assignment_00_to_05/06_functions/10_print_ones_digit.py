def print_ones_digit(num):
    print(f"Ones digit of {num} is {num%10}")
def main():
    num = int(input("Enter Number : "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()