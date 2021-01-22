# Importing OS and CSV
import os 
import csv 

# List to use for the data
financialData = []

# Set the file path for the data 
budget_file = os.path.join("Resources", "budget_data.csv")

# Opening the file path to start working with the data
with open(budget_file, "r") as csvfile:

    # Allow us to read into the data file
    budget_reader = csv.reader(csvfile, delimiter=",")

    # NEED TO SKIP THE HEADER FOR THE FUNCTION TO WORK PROPERLY
    header = next(budget_reader, None)

    # Reading the budget_reader into a new list so we can use the functions we need
    for row in budget_reader:
        financialData.append(row)

    # Formatting
    print("Financial Analysis")
    print("-----------------------------------")

    # get the total number of months in the data set
    total_months = len(financialData)

    print(f"Total Months: {total_months}")

    # Find the total profits in the dataset 
    total_profit_losses = 0

    for months in financialData:                   
        total_profit_losses += int(months[1])

    print(f"Total: ${total_profit_losses}")


    # Calculate the change in "profit/Losses" over the entire period, then find the average of those changes
    # Create a temporary list of just the profits and losses and the change within those profits
    temporary_list = []
    change_in_profits_list = []

    for months in financialData:        
        temporary_list.append(int(months[1])) 

    i = 0 # Using i to be able to signify both the position we are at in the list as well as the next position

    for numbers in range(len(temporary_list) - 1):
        change_in_profits_list.append(int(temporary_list[i+1]) - int(temporary_list[i]))
        i += 1
    
    average_change = sum(change_in_profits_list) / len(change_in_profits_list)

    print(f"Average Change: ${average_change:.2f}")

    # Finding the greatest increase in profits
    greatest_increase_in_profits = max(change_in_profits_list)

    index_increase_change = change_in_profits_list.index(greatest_increase_in_profits) + 1

    print(f"Greatest Increase in Profits: {financialData[index_increase_change][0]} - ${greatest_increase_in_profits}")

    # Finding the greatest decrease in profits
    greatest_decrease_in_profits = min(change_in_profits_list)

    index_decrease_change = change_in_profits_list.index(greatest_decrease_in_profits) + 1

    print(f"Greatest Decrease in Profits: {financialData[index_decrease_change][0]} - ${greatest_decrease_in_profits}")

# file path to write too the analysis folder and csv file
output_path = os.path.join("Analysis", "PyBank_results.csv")

# opening the file to write to it
with open(output_path, 'w') as csvfile:
    # initializing the csv writer
    csvwriter = csv.writer(csvfile, delimiter = ',')

    # outputting the results from PyBank
    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["-----------------------------------"])

    csvwriter.writerow([f"Total Months: {total_months}"])

    csvwriter.writerow([f"Total: ${total_profit_losses}"])

    csvwriter.writerow([f"Average Change: ${average_change:.2f}"])

    csvwriter.writerow([f"Greatest Increase in Profits: {financialData[index_increase_change][0]} - ${greatest_increase_in_profits}"])

    csvwriter.writerow([f"Greatest Decrease in Profits: {financialData[index_decrease_change][0]} - ${greatest_decrease_in_profits}"])