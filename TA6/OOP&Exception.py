class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"

class ItemManagement:
    def __init__(self):
        self.items = {}
        self.next_id = 1

    def create_item(self, name, description, price):
        try:
            if not name or not description:
                raise ValueError("Name and Description cannot be empty.")
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be greater than zero.")
            
            item = Item(self.next_id, name, description, price)
            self.items[self.next_id] = item
            self.next_id += 1
            print(f"Item '{name}' created successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def read_item(self, item_id):
        try:
            item_id = int(item_id)
            if item_id in self.items:
                print(self.items[item_id])
            else:
                print(f"Error: Item with ID {item_id} not found.")
        except ValueError:
            print("Error: Item ID must be a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def update_item(self, item_id, name, description, price):
        try:
            item_id = int(item_id)
            if item_id not in self.items:
                print(f"Error: Item with ID {item_id} not found.")
                return
            
            if not name or not description:
                raise ValueError("Name and Description cannot be empty.")
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be greater than zero.")
            
            item = self.items[item_id]
            item.name = name
            item.description = description
            item.price = price
            print(f"Item '{item_id}' updated successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete_item(self, item_id):
        try:
            item_id = int(item_id)
            if item_id in self.items:
                del self.items[item_id]
                print(f"Item '{item_id}' deleted successfully!")
            else:
                print(f"Error: Item with ID {item_id} not found.")
        except ValueError:
            print("Error: Item ID must be a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def list_items(self):
        if not self.items:
            print("No items found.")
        else:
            for item in self.items.values():
                print(item)

def display_menu():
    print("\nItem Management System:")
    print("[C] - Create Item")
    print("[R] - Read Item")
    print("[U] - Update Item")
    print("[D] - Delete Item")
    print("[L] - List All Items")
    print("[Q] - Quit")

def main():
    item_management = ItemManagement()

    while True:
        display_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'C':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = input("Enter item price: ")
            item_management.create_item(name, description, price)

        elif choice == 'R':
            item_id = input("Enter item ID to view: ")
            item_management.read_item(item_id)

        elif choice == 'U':
            item_id = input("Enter item ID to update: ")
            name = input("Enter new item name: ")
            description = input("Enter new item description: ")
            price = input("Enter new item price: ")
            item_management.update_item(item_id, name, description, price)

        elif choice == 'D':
            item_id = input("Enter item ID to delete: ")
            item_management.delete_item(item_id)

        elif choice == 'L':
            item_management.list_items()

        elif choice == 'Q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
