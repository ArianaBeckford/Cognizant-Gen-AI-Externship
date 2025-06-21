inventory = {}
run = True
while(run):
    print("Welcome to the Inventory Manager!")
    print("Please choose an action: ") #user gets to choose specific action
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. View inventory")
    print("5. Calculate total value")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        item_name = input("Enter item name: ")
        if item_name in inventory: #prevents user from adding same item
            print("This item is already in the inventory, please add a different item.")
        else:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.update({item_name: (quantity, price)})
    elif choice == '2':
        if not inventory: #doesn't allow user to remove item from empty inventory
            print("The inventory is currently empty, there are no items to remove.")
        else:
            item_name = input("Enter the item name to remove: ")
            if item_name in inventory:
                removed_item = inventory.pop(item_name) #use pop() to remove item
                print("Removing item: " + item_name)
            else: #doesn't allow user to remove item that's not in the inventory
                print(f"{item_name} not found in inventory.")
    elif choice == '3':
        if not inventory: #doesn't allow user to update item from empty inventory
            print("The inventory is currently empty, there are no items to update.")
        else:
            item_name = input("Enter the item name to update: ")
            if item_name in inventory: #user gets choice of updating quantity, price, or both
                print("Updating item: " + item_name)
                curr_quant, curr_price = inventory[item_name]
                update_choice = input("Update (q)uantity, (p)rice, or (b)oth: ")
                if update_choice == 'q':
                    new_quant = int(input("Enter the new quantity: "))
                    inventory[item_name] = (new_quant, curr_price)
                elif update_choice == 'p':
                    new_price = float(input("Enter the new price: "))
                    inventory[item_name] = (curr_quant, new_price)
                elif update_choice == 'b':
                    new_quant = int(input("Enter the new quantity: "))
                    new_price = float(input("Enter the new price: "))
                    inventory[item_name] = (new_quant, new_price)
                else:
                    print("Invalid choice, please enter 'q', 'p', or 'b'.")
            else: #doesn't allow user to update item not found in inventory
                print(f"{item_name} not found in inventory.")
    elif choice == '4': #displays inventory every time user chooses option 4
        print("Current inventory: ") #for loop used to display items
        for item_name, (quantity, price) in inventory.items():
            print(f"Item: {item_name}, Quantity: {quantity}, Price: ${price}")
    elif choice == '5':
        total = 0 #for loop used to calcuate total
        for item_name, (quantity, price) in inventory.items():
            total += quantity * price
        print(f"Total value of inventory: ${total:.2f}") #:.2f formats total to 2 decimal places
    elif choice == '6':
        print("Thank you for using the Inventory Manager!")
        print("Exiting program.")
        run = False
    else:
        print("Invalid option. Please choose between 1 and 6.")

    
        
