FAHRENHEIT_OFFSET = 32
FAHRENHEIT_SCALE = 1.8


def fahrenheit_to_celsius(value: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (value - FAHRENHEIT_OFFSET) / FAHRENHEIT_SCALE


def celsius_to_fahrenheit(value: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (value * FAHRENHEIT_SCALE) + FAHRENHEIT_OFFSET


def get_valid_number(prompt: str) -> float:
    """Prompt the user for a valid float or integer."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Enter only float or integer values.")


def get_valid_temperature_scale() -> str:
    """Prompt the user for a valid temperature scale (C/F)."""
    while True:
        temperature_scale = (
            input("Please enter the temperature scale you prefer (C/F): ")
            .strip()
            .lower()
        )
        if temperature_scale in ("f", "c"):
            return temperature_scale
        print("Invalid input! Enter only C or F.")


def main():
    print("Welcome to the Temperature Conversion App 🔥🔥")
    while True:
        temperature_scale = get_valid_temperature_scale()
        temperature = get_valid_number("Enter the temperature: ")

        if temperature_scale == "f":
            result = round(fahrenheit_to_celsius(temperature), 2)
            print(f"{temperature} °F = {result} °C")
        else:
            result = round(celsius_to_fahrenheit(temperature), 2)
            print(f"{temperature} °C = {result} °F")

        again = input("Do you want to convert again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Thank you for using the app!\nMade with ♥ by Majed Abumathkour")


if __name__ == "__main__":
    main()
