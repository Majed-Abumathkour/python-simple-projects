def calculator(operator: str, value_1, value_2):
    match operator:
        case "+":
            result = value_1 + value_2
        case "-":
            result = value_1 - value_2
        case "/":
            result = value_1 / value_2
        case "*":
            result = value_1 * value_2
        case _:
            return calculator(
                input(
                    f"{operator} is a Wrong Operator!!\nOnly these operators (+ - / *) are allowed\nEnter a valid operator: "
                ),
                value_1,
                value_2,
            )
    return f"the result of {value_1} {operator} {value_2} = {round(result, 2)}"


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number (integer or float).")


operator = input("Enter an operator (+ - / *): ")
value_1 = get_number("Enter value 1: ")
value_2 = get_number("Enter value 2: ")
print(calculator(operator, value_1, value_2))
