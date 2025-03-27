def main():
    try:
        f_temp = float(input("Enter the temperature in Fahrenheit : "))
        c_temp = (f_temp - 32) * (5.0/9.0)
        print(f"Temperature: {f_temp}F = {c_temp:.4}C")
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()