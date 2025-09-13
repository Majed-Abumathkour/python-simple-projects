def get_item() -> dict:
    item_name = input(f"Enter the Item Name: ").strip().lower()
    while True:
        try:
            item_price = float(input(f"Enter {item_name.capitalize()}'s Price: "))
            break
        except ValueError:
            print("⚠ The price must be a numeric value!")
    return {item_name: item_price}


def get_cart() -> dict:
    cart = {}
    while True:
        item = get_item()
        item_name = next(iter(item.keys()))
        # Check if item exists
        if item_name in cart:
            if cart[item_name] == item[item_name]:
                print(f"❌ {item_name.capitalize()} cannot be added to the cart because it already exists.")
                continue
            else:
                print(f"⚠ {item_name.capitalize()} already exists in the cart, but at a different price.")
                choice = input("Do you want to update the price? (y/n): ").lower().strip()
                if choice == "y" or choice == "yes":
                    cart.update(item)
                    print(f'✅ The Price of "{item_name.capitalize()}" was updated.')
                else:
                    print(f'❎ The Price of "{item_name.capitalize()}" was not updated')
        else:
            cart.update(item)
        exit_choice = input(f"Do you want to exit? (y/n): ").lower().strip()
        if exit_choice == "y" or exit_choice == "yes":
            break
    return cart


def calculate_total(cart: dict) -> float:
    total = 0
    for value in cart.values():
        total += value
    return total


def print_cart(cart: dict):
    if not cart:
        print("🛒 Your cart is empty.")
        return
    print("\n🛒 Your Shopping Cart:")
    print("-----------------------------")
    print(f"{'Item':<20} {'Price':>8}")
    print("-----------------------------")
    for item, price in cart.items():
        print(f"{item.capitalize():<20} {price:>7.2f}$")
    print("-----------------------------")
    total = calculate_total(cart)
    print(f"{'Total':<20} {total:7.2f}$")
    print("-----------------------------")


def main():
    print("----------------------------------------")
    print("Welcome to the shopping cart program 👋👋")
    print("----------------------------------------")
    cart = get_cart()
    print_cart(cart)


if __name__ == "__main__":
    main()
