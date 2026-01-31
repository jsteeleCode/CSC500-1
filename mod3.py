# ask the user for their name
employeeName = input("which employee do you want leave dates for, Kathy, Frank, Isaac or Rosa:  ")

# #make dict with names as keys and leave dates in nested lists
employeeLeave = { 
    "Kathy": ["Jan 05", "Feb 13", "Mar 08", "Apr 21"],
    "Frank": ["Jan 11", "Feb 22", "Mar 10", "Apr 16"],
    "Isaac": ["Jan 20", "Feb 15", "Mar 21", "Apr 07"],
    "Rosa": ["Jan 18", "Feb 11", "Mar 02", "Apr 01"] 
      }

# display the leave dates for the requested employee
print("The leave dates for", employeeName, "are:", employeeLeave.get(employeeName, "Employee not found"))

#end of program

