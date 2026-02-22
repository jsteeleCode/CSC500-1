# For this one i will make a shopping cart program that uses a class to create items and allow a user to interact with the cart and the items.

class ShoppingCart:
    # make attributes for the class - name, date and cart items
    customerName = ""
    date = ""
    cartItems = []

    #class default constructor for innitializing the attributes
    def __init__(self, customerName, date):
        self.customerName = customerName
        self.date = date

    #class methods
    def addItem(self,itemToPurchase, itemPrice):
        self.cartItems.append((itemToPurchase, itemPrice))

    #method removes item from the cartItems list
    def removeItem(self, itemName):
        self.cartItems = [item for item in self.cartItems if item[0] != itemName]
        #if an item cannot be found, print a message to the user
        if not any(item[0] == itemName for item in self.cartItems):
            print(f"item not found in the cart.")

    #modify item method with a itemToPurchase and newPrice
    def modifyItem(self, itemToPurchase, newPrice):
        #if item can be found by name, check if perameter has default values for description, price and quantity.
        for i, item in enumerate(self.cartItems):
            if item[0] == itemToPurchase:
                if newPrice != 0.0:
                    self.cartItems[i] = (itemToPurchase, newPrice)
                else:
                    print(f"item not found in the cart.")
                break

    # method to get num items in the cart
    def getNumItemsInCart(self):
        return len(self.cartItems)
    
    # method to calculate the total cost of the items in the cart
    def getCostOfCart(self):
        totalCost = 0.0
        for item in self.cartItems:
            totalCost += item[1]
        return totalCost
    
    # method to output total of the items in the cart 
    def printTotal(self):
        print(f"{self.customerName}'s Shopping Cart - {self.date}")
        print(f"Number of Items: {self.getNumItemsInCart()}\n")
        for item in self.cartItems:
            print(f"{item[0]}: ${item[1]:.2f}")
        print(f"\nTotal: ${self.getCostOfCart():.2f}")

    # print an items description method
    def printDescriptions(self):
        print(f"{self.customerName}'s Shopping Cart - {self.date}")
        print(f"Number of Items: {self.getNumItemsInCart()}\n")
        for item in self.cartItems:
            print(f"{item[0]}: ${item[1]:.2f}")

#main function
def main():
    # implement a printMenu function with a shoppingcart parameter that prints the menu options for the user and takes in their choice.
    def printMenu(cart):
        print(f"\nMENU\n")
        print(f"a - Add an item to cart")
        print(f"r - Remove an item from the cart")
        print(f"c - Change the item quantity")
        print(f"d - Output descriptions of all the junk in the cart")
        print(f"o - Output shopping cart contents")
        print(f"q - Quit\n")
        #if an invalid option is chosen, print a message to the user and ask them to choose again until they choose a valid option
        valid_options = ['a', 'r', 'c', 'd', 'o', 'q']
        while True:
            choice = input("Choose an option: ")
            if choice in valid_options:
                break
            else:
                print("Invalid option. Please choose again.")
        return choice
    
    # based on their choice, call the appropriate method from the shopping cart class.
    customerName = input("Enter the customer's name pretty please: ")
    date = input("now plz Enter today's date: ")
    cart = ShoppingCart(customerName, date)
    while True:
        choice = printMenu(cart)
        if choice == 'a':
            itemName = input("Enter the name of the item you got (u better remember all the spelling for later): ")
            itemPrice = float(input("Enter the item price in Australian dollaridoos: "))
            cart.addItem(itemName, itemPrice)
        elif choice == 'r':
            itemName = input("Enter the name of the item you want to destroy: ")
            cart.removeItem(itemName)
        elif choice == 'c':
            itemName = input("Enter the name of the item you want to ruin with all your changes: ")
            newPrice = float(input("Enter the new price (in Ausi bucks of course): "))
            cart.modifyItem(itemName, newPrice)
        elif choice == 'd':
            cart.printDescriptions()
        elif choice == 'o':
            cart.printTotal()
        elif choice == 'q':
            break

#call main function
main()

#end of program
    


