
# create nested loops to collect data and calculate the average rainfall over a period of years.
#-----------------------------------------------------------------------------------------------

# ask the user for number of years.
num_years = int(input("Enter the number of years: "))

# set the rainfall variable
total_rainfall = 0

# loop through each year
for year in range(1, num_years + 1):
    # just define 12 months per year. Im doing this so I could change it later if we wanted to ask a user for months.
    num_months = int(12)

    # loop through each month
    for month in range(1, num_months + 1):
        # ask the user for the rainfall for the current month
        rainfall = float(input(f"Enter the rainfall in inches for month {month} of year {year}: "))
        # add the rainfall to the total
        total_rainfall += rainfall

# calculate the average rainfall
average_rainfall = total_rainfall / (num_years * num_months)

# display the number of months
print(f"The total number of months is: {num_years * num_months}")

# show the total rainfall
print(f"The total rainfall over {num_years} years is: {total_rainfall:.2f} inches")

# display the average rainfall
print(f"The average rainfall over {num_years} years is: {average_rainfall:.2f}")



