# Define the menu with more food items
menu = {
    "pizza": 60,
    "pasta": 90,
    "burger": 70,
    "coffee": 80,
    "ice cream": 40,
    "chocolate donut": 60,
    "sandwich": 50,
    "salad": 45,
    "tea": 30,
    "juice": 55
}

# Display the menu and welcome message
print("Welcome to the hotel!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

# Initialize the total order amount and ordered items dictionary
total_order = 0
order_summary = {}

# Function to process the order
def add_item_to_order(item, quantity):
    global total_order
    if item in menu:
        cost = menu[item] * quantity
        total_order += cost
        if item in order_summary:
            order_summary[item] += quantity
        else:
            order_summary[item] = quantity
        print(f"Your item {item} (x{quantity}) has been added to your order.")
    else:
        print(f"Sorry, {item} is not available yet.")

# Function to remove an item from the order
def remove_item_from_order(item, quantity):
    global total_order
    if item in order_summary:
        if order_summary[item] >= quantity:
            cost = menu[item] * quantity
            total_order -= cost
            order_summary[item] -= quantity
            if order_summary[item] == 0:
                del order_summary[item]
            print(f"{quantity} of {item} has been removed from your order.")
        else:
            print(f"Cannot remove more {item} than what was ordered.")
    else:
        print(f"{item} is not in your order.")

# Function to apply a discount
def apply_discount(discount_percentage):
    global total_order
    discount_amount = total_order * (discount_percentage / 100)
    total_order -= discount_amount
    return discount_amount

# Input items and quantities
def get_order_item():
    item = input("Enter the name of the item you want to order: ").lower()
    quantity = int(input(f"How many {item}s would you like to order? "))
    return item, quantity

# Add the first item to the order
item_1, quantity_1 = get_order_item()
add_item_to_order(item_1, quantity_1)

# Ask if the user wants to add another item
while True:
    another_order = input("Do you want to add another item? (yes/no): ").lower()
    if another_order == "yes":
        item, quantity = get_order_item()
        add_item_to_order(item, quantity)
    elif another_order == "no":
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")

# Option to remove an item
remove_order = input("Do you want to remove an item from your order? (yes/no): ").lower()
if remove_order == "yes":
    item_to_remove = input("Enter the name of the item you want to remove: ").lower()
    quantity_to_remove = int(input(f"How many {item_to_remove}s do you want to remove? "))
    remove_item_from_order(item_to_remove, quantity_to_remove)

# Option to apply a discount
apply_discount_option = input("Do you have a discount code? (yes/no): ").lower()
if apply_discount_option == "yes":
    discount_percentage = float(input("Enter the discount percentage: "))
    discount_amount = apply_discount(discount_percentage)
    print(f"A discount of Rs{discount_amount:.2f} has been applied.")

# Print the total amount and order summary
print("\nOrder Summary:")
for item, quantity in order_summary.items():
    print(f"{item}: {quantity} x Rs{menu[item]}")

print(f"\nThe total amount of your order is Rs{total_order:.2f}.")
