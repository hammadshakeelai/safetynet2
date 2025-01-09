# Restaurant Menu and Ordering System

# Menu stored as a dictionary
menu = {
    "Pizza": 45678.9345679,
    "Burger": 5.49,
    "Pasta": 7.99,
    "Salad": 4.99,
    "Soda": 1.99,
    'ice cube': 0.01
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:,.2f}")

def take_order():
    order = {}
    while True:
        item = input("Enter the name of the item to order (or 'done' to finish): ").capitalize()
        if item == "Done":
            break
        elif item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not found on the menu. Please try again.")
    return order

def generate_receipt(order):
    print("\nReceipt:")
    total = 0
    for item, quantity in order.items():
        price = menu[item] * quantity
        print(f"{item} x {quantity} = ${price:.2f}")
        total += price
    print(f"\nTotal: ${total:.2f}")

# Main program
print("Welcome to the Restaurant!")
display_menu()
order = take_order()
if order:
    generate_receipt(order)
else:
    print("No items ordered. Thank you!")
