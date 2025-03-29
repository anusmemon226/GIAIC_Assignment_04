def add_three_copies(text,myList):
    for _ in range(3):
        myList.append(text)

def main():
    message = input("Enter message to copy : ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(message, my_list)
    print("List after:", my_list)

if __name__ == "__main__":
    main()