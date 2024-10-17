# PyBank
import csv
import os
resource_file = os.path.join("Resources", "budget_data.csv")
analysis_file = os.path.join("Analysis", "budget_analysis.txt")

# Define variables to track financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
increase = 0
decrease = 0
change = 0

# Open and read the csv
with open(resource_file) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    
    #Track the total and net change
    total_net = int(first_row[1])
    previous_profit = int(first_row[1])

    # Process each row of data
    for row in reader:
        total_months = total_months + 1
        profit = int(row[1])
        total_net = int(total_net) + profit

        # Track change
        change = change + (profit - previous_profit)


        # Track biggest increase/decrease
        if increase < (profit - previous_profit):
            increase = (profit - previous_profit)
            increase_month = row[0]
        if decrease > (profit - previous_profit):
            decrease = (profit - previous_profit)
            decrease_month = row[0]

        # Store new previous_profit
        previous_profit = int(row[1])

    # Calculate average change/month
    avg_change = (change/total_months)
    

# Generate the output summary
output = (f"""Total Months: {total_months + 1}
Total: ${total_net}
Average change/month: $({avg_change:.2f})
Greatest Increase in Profits: {increase_month} (${increase})
Greatest Decrease in Profits: {decrease_month} (${decrease})""")

# Print the output
print(output)

# Write the results to a text file
with open(analysis_file, "w") as txt_file:
    txt_file.write(output)