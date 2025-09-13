def kg_to_pound(value):
    return round(value * 2.20462, 2)


def pound_to_kg(value):
    return round(value * 0.453592, 2)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_choice():
    while True:
        choice = input(
            "1- to convert kgs to pounds\n2- to convert pounds to kgs\nEnter your choice: "
        )
        if choice in ("1", "2"):
            return choice
        print("Invalid input! Enter only 1 or 2.")


def main():
    choice = get_choice()
    value = get_number("Enter the weight: ")

    if choice == "1":
        result = kg_to_pound(value)
        print(f"{value} kg = {result} pound")
    else:
        result = pound_to_kg(value)
        print(f"{value} pound = {result} kg")


if __name__ == "__main__":
    main()
