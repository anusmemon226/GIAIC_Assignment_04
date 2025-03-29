def get_first_element(lst):
    print(lst[0])

def get_lst():
    lst = []
    try:
        elemLen = int(input("Enter length of List : "))
    except ValueError:
        print("Invalid Input")
    for i in range(elemLen):
        elem = input(f"Please enter an {i+1} element of the list : ")
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()