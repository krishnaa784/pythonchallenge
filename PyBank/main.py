# financial_analysis.py

import csv
import os

# Define file paths
input_file = 'C:/Users/preit/OneDrive/Desktop/pythonchallenge/PyBank/Resources/budget_data.csv'
output_file = 'C:/Users/preit/OneDrive/Desktop/pythonchallenge/PyBank/analysis/financial_analysis_results.txt'

def analyze_financial_data():
    # Initialize variables
    total_months = 0
    net_profit_loss = 0
    previous_profit_loss = 0
    changes = []
    months = []
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Read the CSV file
    with open(input_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row

        for row in csvreader:
            month = row[0]
            profit_loss = int(row[1])

            total_months += 1
            net_profit_loss += profit_loss
            
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                months.append(month)
            
            previous_profit_loss = profit_loss

    # Calculate the average change
    average_change = sum(changes) / len(changes) if changes else 0

    # Find greatest increase and decrease
    greatest_increase = max(changes) if changes else 0
    greatest_decrease = min(changes) if changes else 0
    greatest_increase_month = months[changes.index(greatest_increase)] if changes else ""
    greatest_decrease_month = months[changes.index(greatest_decrease)] if changes else ""

    # Print and write results to file
    with open(output_file, 'w') as outfile:
        outfile.write(f"Total Months: {total_months}\n")
        outfile.write(f"Total Profit/Losses: ${net_profit_loss}\n")
        outfile.write(f"Average Change: ${average_change:.2f}\n")
        outfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
        outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
        
    print(f"Total Months: {total_months}")
    print(f"Total Profit/Losses: ${net_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

if __name__ == "__main__":
    analyze_financial_data()

