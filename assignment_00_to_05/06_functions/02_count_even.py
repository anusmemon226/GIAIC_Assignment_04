def count_even(lst):
    evenCount = sum([1 for num in lst if num % 2 == 0])
    return evenCount

def main():
    lst = []
    num = input("Enter an integer or press enter to stop : ")
    while num:
        lst.append(int(num))
        num = input("Enter an integer or press enter to stop : ")
    print(count_even(lst))

if __name__ == "__main__":
    main()