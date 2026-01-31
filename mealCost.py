#ask the user how much their meal did cost
mealCost = float(input("Enter the cost of your meal before tax and tip: "))

#calculate the tax amount (7%)
taxAmount = mealCost * 0.07

#calculate the tip amount (18%)
tipAmount = mealCost * 0.18

#calculate the total cost of the meal
totalCost = mealCost + taxAmount + tipAmount

#display the total cost of the meal
print("The total cost of your meal, including tax and tip, is: $", totalCost)

#end of program

