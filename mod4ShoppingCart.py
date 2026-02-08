#creat an itemToPurchase class
class ItemToPurchase:
    #creat attributes   
    itemName = ""
    itemPrice = float()
    itemQuantity = int()

    #default constructor
def __init__(self, itemName="none", itemPrice=0.0, itemQuantity=0):
    self.itemName = itemName
    self.itemPrice = itemPrice
    self.itemQuantity = itemQuantity  

#method to print the cost of the thingsssss!
def printItemCost(self):
    totalCost = self.itemPrice * self.itemQuantity
    print(f"At {self.itemPrice} dollars per {self.itemName} and {self.itemQuantity} total {self.itemName}s = ${totalCost}")

    # set innit method to the class
ItemToPurchase.__init__ = __init__
ItemToPurchase.printItemCost = printItemCost

#main function
def main():
    #create two things of the itemToPurchase class
    thing1 = ItemToPurchase()
    thing2 = ItemToPurchase()

    #get user input for thing 1
    print("Item 1")
    thing1.itemName = input("Enter the item name: ")
    thing1.itemPrice = float(input("Enter the item price: "))
    thing1.itemQuantity = int(input("Enter the item quantity: "))

    #get user input for thing 2
    print("\nItem 2")
    thing2.itemName = input("Enter the item name: ")
    thing2.itemPrice = float(input("Enter the item price: "))
    thing2.itemQuantity = int(input("Enter the item quantity: "))

    #print the total cost of the things
    print("\nTOTAL COST OF OBJECT 1")
    thing1.printItemCost()
    print("\nAND TOTAL COST OF OBJECT 2") 
    thing2.printItemCost()
    print("\n")

#add the total cost of the two things together and print it out
    completeTotalCost = (thing1.itemPrice * thing1.itemQuantity) + (thing2.itemPrice * thing2.itemQuantity)
    print(f"The total cost of the two things is: ${completeTotalCost}")  

#call main function
main()

#end of program

