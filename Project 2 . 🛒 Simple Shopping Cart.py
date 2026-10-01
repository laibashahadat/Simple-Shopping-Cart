# 🛒 Simple Shopping Cart

# -----------------------------------
# Shopping Cart
# -----------------------------------

cart = []


# -----------------------------------
# Add Item Function
# -----------------------------------

def Add_item():

    item = input("Enter item to add: ")
    price = int(input("Enter price of item: "))

    cart.append({
        "item": item,
        "price": price
    })

    print("Item added successfully")


# -----------------------------------
# Remove Item Function
# -----------------------------------

def Remove_item():

    item = input("Enter item to remove: ")

    for cart_item in cart:

        if cart_item["item"] == item:

            cart.remove(cart_item)

            print("Item removed successfully")
            return

    print("Item not found")


# -----------------------------------
# Show Cart Function
# -----------------------------------

def Show_cart():

    if not cart:

        print("Your cart is empty")

    else:

        print("\nYour cart items are:")

        for cart_item in cart:

            print(
                "Item:", cart_item["item"],
                "Price:", cart_item["price"]
            )


# -----------------------------------
# Total Price Function
# -----------------------------------

def Total_price():

    total = 0

    for cart_item in cart:

        total = total + cart_item["price"]

    print("Total price of items in cart is:", total)


# ===================================
# Main Program
# ===================================

while True:

    print("\n==============================")
    print("     Welcome to Shopping Cart")
    print("==============================")

    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Cart")
    print("4. Total Price")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        Add_item()

    elif choice == "2":

        Remove_item()

    elif choice == "3":

        Show_cart()

    elif choice == "4":

        Total_price()

    elif choice == "5":

        print("Thank you for using Shopping Cart ❤️")
        break

    else:

        print("Invalid choice, please try again.")