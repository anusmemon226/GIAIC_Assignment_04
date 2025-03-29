def main():
    adjective = input("Please type an adjective and press enter : ")
    verb1 = input("Please type a verb and press enter : ")
    verb2 = input("Please type a verb and press enter : ")
    famous_person = input("Please type famous person : ")
    SENTENCE_START = f"Computer programming is so {adjective}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
    print(SENTENCE_START)
if __name__ == '__main__':
    main()