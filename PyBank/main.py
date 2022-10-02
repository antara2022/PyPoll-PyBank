# Creating a Python script that analyzes the financial records of your company

# Import os module
import os

# Import module for reading CSV files
import csv

# create a path to the file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
months = []
profit_and_losses = []

# Set start conditions
total_months = 0
net_profit_losses = 0
last_months_profit_loss = 0
current_months_profit_loss = 0
change_in_profit_loss = 0

# Using CSV module to read in csv

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Print header
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
    
        # Number of months
        total_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_months_profit_loss = int(row[1])
        net_profit_losses += current_months_profit_loss

        if (total_months == 1):
            # Set value of last month's profit/loss to be equal to current month's profit/loss
            last_months_profit_loss = current_months_profit_loss
            continue

        else:

            # Calculate change in "Profit/Losses"
            change_in_profit_loss = current_months_profit_loss - last_months_profit_loss

            # Add each month
            months.append(row[0])

            # Add each profit/loss change
            profit_and_losses.append(change_in_profit_loss)

            # Set current month's profit/loss to be last month's profit/loss in next loop
            last_months_profit_loss = current_months_profit_loss

        # The sum and average of the changes in "Profit/Losses" over the entire period
        sum_profit_losses = sum(profit_and_losses)
        average_profit_losses = round(sum_profit_losses/(total_months - 1), 2)

        # Calculate greatest increase and decrease in profits over the entire period
        greatest_increase = max(profit_and_losses)
        greatest_decrease = min(profit_and_losses)

        # Find the index value of the greatest increase and decrease in profits over the entire period
        greatest_increase_month_index = profit_and_losses.index(greatest_increase)
        greatest_decrease_month_index = profit_and_losses.index(greatest_decrease)

        # Find months with greatest increase and decrease in profits
        greatest_increase_month = months[greatest_increase_month_index]
        greatest_decrease_month = months[greatest_decrease_month_index]

        # Print out the analysis to the terminal
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${net_profit_losses}")
        print(f"Average Change: ${average_profit_losses}")
        print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
        print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
        
        # Specify the text file to export the results to
        budget_analysis_results = os.path.join("analysis", "budget_analysis_results.txt")

        # Open the file using the "write" mode and specifiy the variable to hold the contents
        with open(budget_analysis_results, 'w') as textfile:

            textfile.write("Financial Analysis\n")
            textfile.write("----------------------------\n")
            textfile.write(f"Total Months: {total_months}\n")
            textfile.write(f"Total: ${net_profit_losses}\n")
            textfile.write(f"Average Change: ${average_profit_losses}\n")
            textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
            textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")