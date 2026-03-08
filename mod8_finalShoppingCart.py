# create an object of type shopping cart
class ShoppingCart:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.description} - ${self.price} x {self.quantity} = ${self.total_price()}"
    
    #function to remove item from cart
    def remove_item(self):
        self.quantity = 0
        print(f"{self.name} has been removed from the cart.")

    #function to add item to cart
    def add_item(self, quantity):
        self.quantity += quantity
        print(f"{quantity} {self.name}(s) have been added to the cart. Total quantity: {self.quantity}")

    #function to change item quantity in cart
    def change_quantity(self, quantity):
        self.quantity = quantity
        print(f"The quantity of {self.name} has been changed to {self.quantity}.")
        
#main function
def main():
    #ask user for users name and the date. then show them the menu options to add, remove or change quantity of items in the cart.
    user_name = input("Please enter your name: ")
    date = input("Please enter the date (MM/DD/YYYY): ")
    print(f"Welcome {user_name}! Today's date is {date}.")
    print("Menu Options:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Change item quantity in cart")
    cart = []
    while True:
        option = input("Please select an option (1, 2, 3) or 'q' to quit: ")
        if option == '1':
            name = input("Enter the item name: ")
            price = float(input("Enter the item price: "))
            description = input("Enter the item description: ")
            quantity = int(input("Enter the item quantity: "))
            item = ShoppingCart(name, price, description, quantity)
            cart.append(item)
            print(f"{item} has been added to the cart.")
        elif option == '2':
            name = input("Enter the item name to remove: ")
            for item in cart:
                if item.name == name:
                    item.remove_item()
                    cart.remove(item)
                    break
            else:
                print(f"{name} not found in the cart sry.")
        elif option == '3':
            name = input("Enter the item name to change quantity: ")
            for item in cart:
                if item.name == name:
                    quantity = int(input("Enter the new quantity: "))
                    item.change_quantity(quantity)
                    break
            else:
                print(f"{name} not found in the cart.")
        elif option.lower() == 'q':
            print("Thank you, comeagain!")
            break
        else:
            print("Invalid option. go again.")

if __name__ == "__main__":
    main()

