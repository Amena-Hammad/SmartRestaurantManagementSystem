# -*- coding: utf-8 -*-
"""
Smart Restaurant Management System
"""

from datetime import datetime

# =========================
# CLASS
# =========================
class RestaurantManager:

    # Default Argument
    def __init__(self, restaurant_name="Smart Restaurant"):
        self.restaurant_name = restaurant_name

        # Dictionary + List
        self.menu = [
            {"id": 1, "name": "Burger", "price": 5.5, "category": "Fast Food", "veg": False},
            {"id": 2, "name": "Pizza", "price": 8.0, "category": "Italian", "veg": False},
            {"id": 3, "name": "Pasta", "price": 7.0, "category": "Italian", "veg": True},
            {"id": 4, "name": "Salad", "price": 4.5, "category": "Healthy", "veg": True},
            {"id": 5, "name": "Fries", "price": 3.0, "category": "Fast Food", "veg": True}
        ]

        self.orders = []

    # =========================
    # FUNCTION WITH PARAMETERS + RETURN
    # =========================
    def calculate_bill(self, subtotal, discount=0):
        total = subtotal - discount
        return total

    # =========================
    # SHOW MENU
    # =========================
    def show_menu(self):

        print(f"\n===== {self.restaurant_name} MENU =====")
        print("ID   Name            Price   Category      Veg")
        print("-" * 55)

        for item in self.menu:

            veg_status = "Yes" if item["veg"] else "No"

            print(
                f"{item['id']}    "
                f"{item['name']}          "
                f"${item['price']}     "
                f"{item['category']}      "
                f"{veg_status}"
            )

    # =========================
    # SEARCH FOOD
    # =========================
    def search_food(self):

        keyword = input("Enter food name to search: ").strip().lower()

        found = False

        for item in self.menu:

            if keyword in item['name'].lower():

                print(f"Found: {item['name']} - ${item['price']}")
                found = True

        if not found:
            print("Food item not found.")

    # =========================
    # ORDER ITEMS
    # =========================
    def order_items(self):

        order_list = []

        while True:

            self.show_menu()

            # Input Validation
            try:

                item_id = int(input("Enter item ID: "))
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

            except ValueError:

                print("Invalid input. Please enter numbers only.")
                continue

            item = next((x for x in self.menu if x['id'] == item_id), None)

            if item:

                total_price = item['price'] * quantity

                order = {
                    "item_name": item['name'],
                    "quantity": quantity,
                    "total_price": total_price,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                order_list.append(order)
                self.orders.append(order)

                print(f"Added {quantity} {item['name']} successfully.")

            else:
                print("Invalid item ID.")
                continue

            more = input("Add more items? (y/n): ").lower()

            if more != 'y':
                break

        # =========================
        # BILL CALCULATION
        # =========================

        subtotal = sum(order['total_price'] for order in order_list)

        # Discount System
        if subtotal >= 30:
            discount = 5

        elif subtotal >= 20:
            discount = 3

        else:
            discount = 0

        # Tax System
        tax = subtotal * 0.05

        # Final Total
        total = self.calculate_bill(subtotal + tax, discount)

        print("\n===== BILL =====")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Final Total: ${total:.2f}")

    # =========================
    # SHOW ORDER HISTORY
    # =========================
    def show_orders(self):

        if not self.orders:

            print("No orders found.")
            return

        print("\n===== ORDER HISTORY =====")

        for order in self.orders:

            print(
                f"{order['item_name']} "
                f"x{order['quantity']} "
                f"= ${order['total_price']} "
                f"({order['time']})"
            )

    # =========================
    # LIST COMPREHENSION
    # =========================
    def expensive_items(self):

        expensive = [
            item['name']
            for item in self.menu
            if item['price'] > 5
        ]

        print("\n===== EXPENSIVE ITEMS =====")

        for item in expensive:
            print(item)

    # =========================
    # 2D LIST
    # =========================
    def sales_table(self):

        sales = [
            ["Burger", 10, 55],
            ["Pizza", 7, 56],
            ["Pasta", 5, 35]
        ]

        print("\n===== SALES TABLE =====")

        for row in sales:
            print(row)

    # =========================
    # SET
    # =========================
    def unique_categories(self):

        categories = set(
            item['category']
            for item in self.menu
        )

        print("\n===== UNIQUE CATEGORIES =====")

        for category in categories:
            print(category)

    # =========================
    # TUPLE
    # =========================
    def min_max_prices(self):

        prices = [item['price'] for item in self.menu]

        result = (min(prices), max(prices))

        print(f"\nLowest Price: ${result[0]}")
        print(f"Highest Price: ${result[1]}")

    # =========================
    # MOST EXPENSIVE ITEM
    # =========================
    def most_expensive_item(self):

        expensive_item = max(
            self.menu,
            key=lambda item: item['price']
        )

        print("\n===== MOST EXPENSIVE ITEM =====")
        print(f"Name: {expensive_item['name']}")
        print(f"Price: ${expensive_item['price']}")

    # =========================
    # ADD NEW PRODUCT
    # =========================
    def add_product(self):

        name = input("Enter food name: ").strip().title()

        try:

            price = float(input("Enter price: "))

            if price <= 0:
                print("Price must be positive.")
                return

        except ValueError:

            print("Invalid price.")
            return

        # Available Categories
        categories = ["Fast Food", "Italian", "Healthy", "Snacks"]
        
        print("\nChoose Category:")
        
        for index, cat in enumerate(categories, start=1):
            print(f"{index}. {cat}")
        
        try:
            category_choice = int(input("Enter category number: "))
        
            if category_choice < 1 or category_choice > len(categories):
                print("Invalid category choice.")
                return
        
            category = categories[category_choice - 1]
        
        except ValueError:
            print("Please enter numbers only.")
            return

        veg_input = input("Is it vegetarian? (y/n): ").lower()

        veg = veg_input == 'y'

        new_item = {
            "id": len(self.menu) + 1,
            "name": name,
            "price": price,
            "category": category,
            "veg": veg
        }

        self.menu.append(new_item)

        print(f"{name} added successfully.")

    # =========================
    # MAIN PROGRAM LOOP
    # =========================
    def run(self):

        while True:

            print("\n===== SMART RESTAURANT MANAGEMENT SYSTEM =====")
            print("1. Show Menu")
            print("2. Order Food")
            print("3. Search Food")
            print("4. Show Orders")
            print("5. Expensive Items")
            print("6. Sales Table")
            print("7. Unique Categories")
            print("8. Min & Max Prices")
            print("9. Most Expensive Item")
            print("10. Add Product")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_menu()

            elif choice == '2':
                self.order_items()

            elif choice == '3':
                self.search_food()

            elif choice == '4':
                self.show_orders()

            elif choice == '5':
                self.expensive_items()

            elif choice == '6':
                self.sales_table()

            elif choice == '7':
                self.unique_categories()

            elif choice == '8':
                self.min_max_prices()

            elif choice == '9':
                self.most_expensive_item()

            elif choice == '10':
                self.add_product()

            elif choice == '0':

                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice.")


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    system = RestaurantManager()
    system.run()