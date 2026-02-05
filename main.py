from utils import (
    add, subtract, multiply, divide,
    check_even_odd, convert_temperature
)

while True:
    print("\n== Terminal Toolkit ==")
    print("1 - Calculator")
    print("2 - Even or Odd")
    print("3 - Temperature Converter")
    print("0 - Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Goodbye!")
        break

    # Calculator block
    if choice == "1":
        print("\n==Calculator==")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")

        op = input("Choose operation: ")

        if op not in ["1", "2", "3", "4"]:
            print("Invalid operation.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input.")
            continue

        if op == "1":
            result = add(a, b)
        elif op == "2":
            result = subtract(a, b)
        elif op == "3":
            result = multiply(a, b)
        elif op == "4":
            result = divide(a, b)
            # If it's an error string, print it directly.
            if isinstance(result, str):
                print(result)
                continue

        print(f"Result: {result}")

    # Even or Odd block
    elif choice == "2":
        print("\n==Even or Odd==")
        try:
            num = int(input("Enter a number: "))
            print(f"{num} is {check_even_odd(num)}.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    # Temperature converter block
    elif choice == "3":
        print("\n==Temperature Converter==")
        try:
            temp = float(input("Enter temperature in Celsius: "))
            print(convert_temperature(temp))
        except ValueError:
            print("Invalid temperature input.")

    else:
        print("Invalid menu option.")