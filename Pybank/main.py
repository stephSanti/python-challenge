import csv

total = 0
months = 0 
prev_profit_losses = None
total_change = 0
num_change = 0
max_increase = 0
max_decrease = 0

# Replace with the actual path of your extracted CSV file
file_path = 'C:/Users/Madelyn Zelaya/Desktop/Starter_Code/PyBank/Resources/budget_data.csv'

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        amount = float(row[1])
        months += 1
        total += amount
        profit_losses = int(row[1])
        month = str(row[0]) #pulls profit/losses value

        if prev_profit_losses is not None: #calculate change from previous row
            change = profit_losses - prev_profit_losses
            total_change += change
            num_change += 1

            if change > max_increase: #if change value is greater than whats stores in max this will update value
                max_increase = change
                max_increase_month = month
            
            if change < max_decrease:
                max_decrease = change
                max_decrease_month = month

        prev_profit_losses = profit_losses #update profit/losses value for next row

average_change = total_change / num_change if num_change else None

print("Financial Analysis")
print("   ")
print("---------------------------------------   ")
print("   ")
print(f'Total Months: {months}')
print(f'Total amount: ${total:.2f}')
print(f'Total Average: {average_change:.2f}')
print(f'Greatest Increase in Profits: {max_increase_month} (${max_increase:.2f})')
print(f'Greatest Decrease in Profits: {max_decrease_month}(${max_decrease:.2f})')