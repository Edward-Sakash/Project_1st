"""#####################################
from data import warehouse1, warehouse2

# Get the user name
user_name = input("What is your user name? ")

# Greet the user
print(f"Hello, {user_name}!")

# Show the menu and ask to pick a choice
print("What would you like to do?")
print("1. List items by warehouse")
print("2. Search an item and place an order")
print("3. Quit")
choice = input("Type the number of the operation: ")

# If they pick 1
if choice == "1":
    print("Items in warehouse 1:")
    for item in warehouse1:
        print("-", item)
    print("Items in warehouse 2:")
    for item in warehouse2:
        print("-", item)

# Else, if they pick 2
elif choice == "2":
    # Ask the user to input an item name and search the warehouses
    item_name = input("What is the name of the item? ")
    total_amount = 0
    location = ""
    max_warehouse = ""
    max_amount = 0

    # Search for the item in warehouse1
    if item_name in warehouse1:
        total_amount += warehouse1.count(item_name)
        location += "Warehouse 1\n"
        if warehouse1.count(item_name) > max_amount:
            max_warehouse = "Warehouse 1"
            max_amount = warehouse1.count(item_name)

    # Search for the item in warehouse2
    if item_name in warehouse2:
        total_amount += warehouse2.count(item_name)
        location += "Warehouse 2\n"
        if warehouse2.count(item_name) > max_amount:
            max_warehouse = "Warehouse 2"
            max_amount = warehouse2.count(item_name)

    # Determine the location and maximum amount
    if total_amount == 0:
        location = "Not in stock"
    elif total_amount > 0 and max_warehouse == "":
        location = "Both warehouses"
    elif max_amount > 0:
        location += f"Maximum availability: {max_amount} in {max_warehouse}"

    print(f"Amount available: {total_amount}")
    print(f"Location: {location}")

    # Ask the user if they want to place an order for this item
    order_choice = input("Would you like to order this item? (y/n) ")

    if order_choice.lower() == "y":
        # Ask the user how many they want to order
        order_amount = int(input("How many would you like? "))

        if order_amount <= total_amount:
            # Sufficient stock available
            print(f"{order_amount} {item_name} have been ordered.")
        else:
            # Insufficient stock available
            print("**************************************************")
            print("There are not this many available. The maximum amount that can be ordered is", total_amount)
            order_max_choice = input("Would you like to order the maximum available? (y/n) ")

            if order_max_choice.lower() == "y":
                # Order the maximum available
                print(f"{total_amount} {item_name} have been ordered.")
            else:
                # User does not want to order
                pass

# Else, if they pick 3
elif choice == "3":
    pass

# Else
else:
    print("**************************************************")
    print("Unsupported operation.")

# Thank the user for the visit
print(f"\nThank you for your visit, {user_name}!")"""


####################################################################
####################################################################
from data_Bonus_1st import stock

# Get the user name
user_name = input("What is your user name? ")

# Greet the user
print(f"Hello, {user_name}!")

# Show the menu and ask to pick a choice
print("What would you like to do?")
print("1. List items by warehouse")
print("2. Search an item and place an order")
print("3. Quit")
choice = input("Type the number of the operation: ")

# If they pick 1
if choice == "1":
    print("Items in warehouse 1:")
    wh1=[item for item in stock if item['warehouse']==1]
    """for item in stock['warehouse1']:
        print("-", item)
    print("Items in warehouse 2:")
    for item in stock['warehouse2']:
        print("-", item)"""
    print(wh1)
    print()


# Else, if they pick 2
elif choice == "2":
    while True:
        # Ask the user to input an item name and search the warehouses
        item_name = input("What is the name of the item? ")
        total_amount = 0
        location = ""
        max_warehouse = ""
        max_amount = 0

        # Search for the item in warehouse1
        if item_name in stock['warehouse1']:
            total_amount += stock['warehouse1'][item_name]
            location += "Warehouse 1\n"
            if stock['warehouse1'][item_name] > max_amount:
                max_warehouse = "Warehouse 1"
                max_amount = stock['warehouse1'][item_name]

        # Search for the item in warehouse2
        if item_name in stock['warehouse2']:
            total_amount += stock['warehouse2'][item_name]
            location += "Warehouse 2\n"
            if stock['warehouse2'][item_name] > max_amount:
                max_warehouse = "Warehouse 2"
                max_amount = stock['warehouse2'][item_name]

        # Determine the location and maximum amount
        if total_amount == 0:
            location = "Not in stock"
        elif total_amount > 0 and max_warehouse == "":
            location = "Both warehouses"
        elif max_amount > 0:
            location += f"Maximum availability: {max_amount} in {max_warehouse}"

        print(f"Amount available: {total_amount}")
        print(f"Location: {location}")

        if total_amount > 0:
            # Ask the user if they want to place an order for this item
            order_choice = input("Would you like to order this item? (y/n) ")

            if order_choice.lower() == "y":
                # Ask the user how many they want to order
                order_amount = int(input("How many would you like? "))

                if order_amount <= total_amount:
                    # Sufficient stock available
                    print(f"{order_amount} {item_name} have been ordered.")
                    # Update the stock in the corresponding warehouse
                    if max_warehouse == "Warehouse 1":
                        stock['warehouse1'][item_name] -= order_amount
                    elif max_warehouse == "Warehouse 2":
                        stock['warehouse2'][item_name] -= order_amount
                else:
                    # Insufficient stock available
                    print("**************************************************")
                    print("There are not this many available. The maximum amount that can be ordered is", total_amount)
                    order_max_choice = input("Would you like to order the maximum available? (y/n) ")

                    if order_max_choice.lower() == "y":
                        # Order the maximum available
                        print(f"{total_amount} {item_name} have been ordered.")
                        # Update the stock in the corresponding warehouse


#################################################################################
#################################################################################
import importlib.util

# Import 'data_Bonus_1st' module
spec = importlib.util.spec_from_file_location("data_Bonus_1st", "data_Bonus_1st.py")
data_Bonus_1st = importlib.util.module_from_spec(spec)
spec.loader.exec_module(data_Bonus_1st)

# Get the 'stock' data from the imported module
stock = data_Bonus_1st.stock

# Get the user name
user_name = input("What is your user name? ")

# Greet the user
print(f"Hello, {user_name}!")

# Show the menu and ask to pick a choice
print("What would you like to do?")
print("1. List items by warehouse")
print("2. Search an item and place an order")
print("3. Quit")
choice = input("Type the number of the operation: ")

# If they pick 1
if choice == "1":
    print("Items in warehouse 1:")
    for item in stock['warehouse1']:
        print("-", item)
    print("Items in warehouse 2:")
    for item in stock['warehouse2']:
        print("-", item)

# Else, if they pick 2
elif choice == "2":
    while True:
        # Ask the user to input an item name and search the warehouses
        item_name = input("What is the name of the item? ")
        total_amount = 0
        location = ""
        max_warehouse = ""
        max_amount = 0

        # Search for the item in warehouse1
        if item_name in stock['warehouse1']:
            total_amount += stock['warehouse1'][item_name]
            location += "Warehouse 1\n"
            if stock['warehouse1'][item_name] > max_amount:
                max_warehouse = "Warehouse 1"
                max_amount = stock['warehouse1'][item_name]

        # Search for the item in warehouse2
        if item_name in stock['warehouse2']:
            total_amount += stock['warehouse2'][item_name]
            location += "Warehouse 2\n"
            if stock['warehouse2'][item_name] > max_amount:
                max_warehouse = "Warehouse 2"
                max_amount = stock['warehouse2'][item_name]

        # Determine the location and maximum amount
        if total_amount == 0:
            location = "Not in stock"
        elif total_amount > 0 and max_warehouse == "":
            location = "Both warehouses"
        elif max_amount > 0:
            location += f"Maximum availability: {max_amount} in {max_warehouse}"

        print(f"Amount available: {total_amount}")
        print(f"Location: {location}")

        if total_amount > 0:
            # Ask the user if they want to place an order for this item
            order_choice = input("Would you like to order this item? (y/n) ")

            if order_choice.lower() == "y":
                # Ask the user how many they want to order
                order_amount = int(input("How many would you like? "))

                if order_amount <= total_amount:
                    # Sufficient stock available
                    print(f"{order_amount} {item_name} have been ordered.")
                    # Update the stock in the corresponding warehouse
                    if max_warehouse == "Warehouse 1":
                        stock['warehouse1'][item_name] -= order_amount
                    elif max_warehouse == "Warehouse 2":
                        stock['warehouse2'][item_name] -= order_amount
                else:
                    # Insufficient stock available
                    
                    print("**************************************************")
                    print("There are not this many available. The maximum amount that can be ordered is", total_amount)
                    order_max_choice = input("Would you like to order the maximum available? (y/n) ")

                    if order_max_choice.lower() == "y":
                        # Order the maximum available
                        print(f"{total_amount} {item_name} have been ordered.")
                        # Update the stock in the corresponding warehouse
                        if max_warehouse == "Warehouse 1":
                            stock['warehouse1'][item_name] -= total_amount
                        elif max_warehouse == "Warehouse 2":
                            stock['warehouse2'][item_name] -= total_amount
                    else:
                        # User does not want to order
                        pass
            else:
                # User does not want to order
                pass

        # Ask the user if they want to search for another item
        search_choice = input("Would you like to search for another item? (y/n) ")
        if search_choice.lower() != "y":
            break

# Else, if they pick 3
elif choice == "3":
    pass

# Else
else:
    print("**************************************************")
    print("Unsupported operation.")

# Thank the user for the visit
print(f"\nThank you for your visit, {user_name}!")

