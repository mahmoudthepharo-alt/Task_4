import json

def save_inventory(data):
    try:
        with open("inventory.json", "w") as file:
            json.dump(data, file)
        print("Inventory saved successfully.")
    except Exception as e:
        print("Error saving inventory:", e)


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No inventory file found. Starting with empty inventory.")
        return {}
    except json.JSONDecodeError:
        print("File is corrupted. Starting fresh.")
        return {}


def manage_inventory():
    inventory = load_inventory()

    while True:
        print("\n--- Inventory Menu ---")
        print("1. View inventory")
        print("2. Add/Update item")
        print("3. Delete item")
        print("4. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if inventory:
                print("\nCurrent Inventory:")
                for item, quantity in inventory.items():
                    print(f"{item}: {quantity}")
            else:
                print("Inventory is empty.")

        elif choice == "2":
            item = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                inventory[item] = quantity
                print(f"{item} updated successfully.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            item = input("Enter item name to delete: ")
            if item in inventory:
                del inventory[item]
                print(f"{item} deleted.")
            else:
                print("Item not found.")

        elif choice == "4":
            save_inventory(inventory)
            print("Exiting inventory manager.")
            break

        else:
            print("Invalid choice. Try again.")


manage_inventory()