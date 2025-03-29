def print_multiple(message,num_of_times):
    for i in range(num_of_times):
        print(message)

def main():
    message = input("Please type a message : ")
    num_of_times = int(input("Enter a number of times to repeat your message : "))
    print_multiple(message,num_of_times)

if __name__ == "__main__":
    main()