# Import os and CSV
import os
import csv

# lists to store month and difference in profit and loss
months = []
diffs_profit_loss = []

# set initial value
months_count = 0
diff_profit_loss = 0
net_total_profit_loss = 0
past_month_profit_loss = 0
present_month_profit_loss = 0

# open and read the csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #read the header row
    csv_header = next(csv_file)
    
    # loop through the data
    for row in csv_reader:
        # sum of months
        months_count = months_count + 1
        
        #append to each month
        months.append(row[0])
        
        #net profit loss for the entire period
        present_month_profit_loss = int(row[1])
        net_total_profit_loss = net_total_profit_loss + present_month_profit_loss
        
        if months_count == 1:
            past_month_profit_loss = present_month_profit_loss
            
        else:
            diff_profit_loss = present_month_profit_loss - past_month_profit_loss
            
            
            diffs_profit_loss.append(diff_profit_loss)
            
            past_month_profit_loss = present_month_profit_loss
            
    # average of change of profit and losses        
    total_profit_loss = sum(diffs_profit_loss)
    average_change_profit_loss = round(total_profit_loss/(months_count - 1), 2)
    
    # greatest increase and decrease in profit
    greatest_increase_profit = max(diffs_profit_loss)
    greatest_decrease_profit = min(diffs_profit_loss)
    
    # index for greatest increase and decrease in profit
    index_greatest_increase_profit = diffs_profit_loss.index(greatest_increase_profit) + 1
    index_greatest_decrease_profit = diffs_profit_loss.index(greatest_decrease_profit) + 1
    
    # date for greatest increase and decrease in profit
    month_greatest_increase_profit = months[index_greatest_increase_profit]
    month_greatest_decrease_profit = months[index_greatest_decrease_profit]
    
    # print statments
    print("Financial Analysis" + "\n")
    print("......................." + "\n")
    print(f"Total Months: {months_count}" + "\n")
    print(f"Total: ${net_total_profit_loss}" + "\n")
    print(f"Average Change: ${average_change_profit_loss}" + "\n")
    print(f"Greatest Increase in Profits: {month_greatest_increase_profit} (${greatest_increase_profit})" + "\n")
    print(f"Greatest Decrease in Profits: {month_greatest_decrease_profit} (${greatest_decrease_profit})" + "\n")
    
    
    # analysis output as text
    output_path = os.path.join("Analysis", "analysis.txt")
    
    with open(output_path, "w") as txtfile:
        txtfile.write("Financial Analysis" + "\n" + "\n")
        txtfile.write("......................." +"\n" + "\n")
        txtfile.write(f"Total Months: {months_count}" + "\n" + "\n")
        txtfile.write(f"Total: ${net_total_profit_loss}" + "\n" + "\n")
        txtfile.write(f"Average Change: ${average_change_profit_loss}" + "\n" + "\n")
        txtfile.write(f"Greatest Increase in Profits: {month_greatest_increase_profit} (${greatest_increase_profit})" + "\n" + "\n")
        txtfile.write(f"Greatest Decrease in Profits: {month_greatest_decrease_profit} (${greatest_decrease_profit})" + "\n" + "\n")
        
    
    






