def main():
    earth_weight = int(input("Enter a weight on Earth : "))
    planet = input("Enter name of planet : ").strip().lower()

    if planet in "mercury":
        print(f"The equivalent weight on {planet} : {round(earth_weight*0.376,2)}")
    elif planet in "venus":
        print(f"The equivalent weight on {planet} : {round(earth_weight*0.889)}")
    elif planet in "mars":
        print(f"The equivalent weight on {planet} : {round(earth_weight*0.378)}")
    elif planet in "jupiter":
        print(f"The equivalent weight on {planet} : {round(earth_weight*2.36)}")
    elif planet in "saturn":
        print(f"The equivalent weight on {planet} : {round(earth_weight*1.081)}")
    elif planet in "uranus":
        print(f"The equivalent weight on {planet} : {round(earth_weight*0.815)}")
    elif planet in "neptune":
        print(f"The equivalent weight on {planet} : {round(earth_weight*1.140)}")
    else:
        print("invalid input")

if __name__ == "__main__":
    main()