def temperature_converter():
    print("=================================")
    print("     TEMPERATURE CONVERTER")
    print("=================================")

    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("\nEnter your choice (1-6): "))
    temp = float(input("Enter temperature value: "))

    if choice == 1:
        result = (temp * 9/5) + 32
        print(f"Fahrenheit = {result:.2f} °F")

    elif choice == 2:
        result = temp + 273.15
        print(f"Kelvin = {result:.2f} K")

    elif choice == 3:
        result = (temp - 32) * 5/9
        print(f"Celsius = {result:.2f} °C")

    elif choice == 4:
        result = (temp - 32) * 5/9 + 273.15
        print(f"Kelvin = {result:.2f} K")

    elif choice == 5:
        result = temp - 273.15
        print(f"Celsius = {result:.2f} °C")

    elif choice == 6:
        result = (temp - 273.15) * 9/5 + 32
        print(f"Fahrenheit = {result:.2f} °F")

    else:
        print("Invalid choice! Please select between 1 and 6.")

temperature_converter()