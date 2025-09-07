def get_positive_float(data_type: str) -> float:
    """
    Prompt the user for a positive float value for the given data type.

    Args:
        data_type (str): The name of the data type to request.

    Returns:
        float: The validated positive float value.
    """
    data_type = data_type.strip().capitalize()
    while True:
        try:
            float_number = float(input(f"Enter the {data_type}: "))
            if float_number < 0:
                print(f"⚠️  {data_type} can't be a negative value!")
                continue
            return float_number
        except ValueError:
            print(
                f"Invalid {data_type}!\n"
                f"⚠️  Note: Please enter a numeric value for {data_type}."
            )


def get_rate() -> float:
    """
    Prompt the user for an interest rate between 0 and 100.

    Returns:
        float: The interest rate as a decimal.
    """
    while True:
        rate = get_positive_float("rate")
        if rate > 100:
            print("⚠️  The interest rate must be at least 0% and at most 100%.")
            continue
        return rate / 100


def get_time() -> float:
    """
    Prompt the user for a time period greater than zero.

    Returns:
        float: The time period in years.
    """
    while True:
        time = get_positive_float("time")
        if time == 0:
            print("⚠️  The Time must be greater than 0.")
            continue
        return time


def get_compounding_frequency() -> int:
    """
    Prompt the user to select a compounding frequency.

    Returns:
        int: The number of compounding periods per year.
    """
    while True:
        print("Choose the compounding frequency 📆:\n1- Yearly\n2- Monthly\n3- Daily")
        choice = input("Please indicate your selection (1, 2, or 3): ").strip()
        match choice:
            case "1":
                return 1
            case "2":
                return 12
            case "3":
                return 365
            case _:
                print("Invalid Input ❌")


def get_compound_interest_data() -> dict:
    """
    Collect all required data for compound interest calculation.

    Returns:
        dict: A dictionary containing principal, rate, time, and compounding frequency.
    """
    compound_interest_data = {}
    compound_interest_data["principal"] = get_positive_float("principal")
    compound_interest_data["rate"] = get_rate()
    compound_interest_data["time"] = get_time()
    compound_interest_data["compounding_frequency"] = get_compounding_frequency()
    return compound_interest_data


def calculate_compound_interest(compound_interest_data: dict) -> float:
    """
    Calculate the compound interest based on the provided data.

    Args:
        compound_interest_data (dict): The input data for calculation.

    Returns:
        float: The calculated compound interest.
    """
    principal = compound_interest_data["principal"]
    rate = compound_interest_data["rate"]
    time = compound_interest_data["time"]
    compounding_frequency = compound_interest_data["compounding_frequency"]
    final_amount = principal * (
        (1 + (rate / compounding_frequency)) ** (time * compounding_frequency)
    )
    compound_interest = final_amount - principal
    return compound_interest


def main() -> None:
    """
    Main loop for the Compound Interest Calculator application.
    """
    frequency_map = {1: "Yearly", 12: "Monthly", 365: "Daily"}
    while True:
        print("------------------------------------")
        print("📈 Welcome to the Compound Interest Calculator App 💡")
        print("------------------------------------")
        compound_interest_data = get_compound_interest_data()
        compound_interest = round(
            calculate_compound_interest(compound_interest_data), 2
        )
        final_value = round(compound_interest + compound_interest_data["principal"], 2)
        frequency = compound_interest_data["compounding_frequency"]
        frequency_str = frequency_map.get(frequency, f"{frequency} times/year")
        print("------------------------------------")
        print(
            f"Compound Interest earned: ${compound_interest}\n"
            f"Final Value of Investment: ${final_value}\n"
            f"Compounding Frequency: {frequency_str}"
        )
        print("------------------------------------")
        want_exit = input("Do you want to exit (Y/N): ")
        if want_exit.strip().lower() == "y":
            break


if __name__ == "__main__":
    main()
