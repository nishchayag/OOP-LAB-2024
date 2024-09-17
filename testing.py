# typing all codes here first to check if they work or not!
def prepare_grocery_bill():
    print("Welcome to the Grocery Bill Generator")
    items = []
    while True:
        item_name = input("Enter the name of the item: ")
        quantity = float(input(f"Enter the quantity of {item_name}: "))
        price_per_unit = float(input(f"Enter the price per unit of {item_name}: "))
        total_cost = quantity * price_per_unit

        items.append((item_name, quantity, price_per_unit, total_cost))
        
        more_items = input("Do you want to add another item? (yes/no): ").strip().lower()
        if more_items != 'yes':
            break
    
    total_amount = sum(item[3] for item in items)
    
    print("\n--- Grocery Bill ---")
    print(f"{'Item Name':<20} {'Quantity':<10} {'Price/Unit':<12} {'Total Cost':<10}")
    print("-" * 52)
    
    for item in items:
        print(f"{item[0]:<20} {item[1]:<10.2f} {item[2]:<12.2f} {item[3]:<10.2f}")
    
    print("-" * 52)
    print(f"{'Total Amount':<42} {total_amount:.2f}")

prepare_grocery_bill()