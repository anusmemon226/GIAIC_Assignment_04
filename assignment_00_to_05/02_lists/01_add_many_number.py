def add_many_numbers(numbers):
    sum = 0
    for number in numbers:
        sum+=number
    return sum
def main():
    listLen = int(input("How many numbers : "))
    numbers = []
    for i in range(listLen):
        try:
            num = int(input(f"Enter Number {i+1} : "))
            numbers.append(num)
        except ValueError:
            print("Invalid Input")
            break
    print(f"Sum of {numbers} is : {add_many_numbers(numbers)}")

if __name__ == "__main__":
    main()