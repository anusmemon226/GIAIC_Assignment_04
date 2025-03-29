import time

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        print(divmod(t,60))
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1

def main():
    t = input("Enter time in seconds : ")
    countdown(int(t))

if __name__ == "__main__":
    main()