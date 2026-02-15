#ask the user to enter the number of books that they have purchased this month and then display the number of points awarded.
#-----------------------------------------------------------------------------------------------

# ask the user for the number of books purchased. If they enter anything other than 0,2,4, 6, or 8, ask them to enter a valid number of books.
num_books = int(input("Enter the number of books you have purchased this month: "))
while num_books not in [0, 2, 4, 6, 8]:
    num_books = int(input("Sorry - invalid number of books. Please enter 0, 2, 4, 6, or 8: "))

# determine the number of points awarded based on the number of books purchased
if num_books == 0:
    points = 0
elif num_books == 2:
    points = 5
elif num_books == 4:
    points = 15
elif num_books == 6:
    points = 30
elif num_books == 8:
    points = 60

# display the number of points awarded
print(f"Wonderful! you have been awarded {points} points for purchasing {num_books} books this month.")



