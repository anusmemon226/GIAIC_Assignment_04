def main():
    mass = float(input("Enter mass in kg : "))
    c = 299792458
    e = mass * c**2
    print(f"{e} joules of energy!")

if __name__ == "__main__":
    main()