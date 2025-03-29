def count_numbers(numbers_list):
    count_dict = {}
    for number in numbers_list:
        if number not in count_dict:
            count_dict[number] = 1
        else:
            count_dict[number] += 1
    return count_dict
def main():
    number_list = []
    while True:
        userInput = input("Enter Number : ")

        if userInput == "":
            break

        number_list.append(int(userInput))
    
    count_dict = count_numbers(number_list)
    print(count_dict)

if __name__ == "__main__":
    main()

