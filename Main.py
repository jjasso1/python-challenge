import os
import csv

csvpath = os.path.join("C:/Users/jasso/Bootcamp/pybank_hw/resources/budget_data.csv")

total_months = 0
total_net = 0 
change_per_month = []
net_change_list = []
amount = 0
greatest_increase = 0
increase_month = ''
greatest_decrease = 0
decrease_month = ''

with open(csvpath, 'r') as file_handler:
    csvreader = csv.reader(file_handler,delimiter=',')
    
    header = next(reader)

    first_row = next(reader)
    total_months = +=1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_months +=1
        total_net += int(first_row[1])

        change_from_last_month = int(csv_data[i][1]) - int(csv_data[i-1][1])
        if change_from_last_month > greatest_increase:
            greatest_increase = change_from_last_month
            increase_month = csv_data[i][0] 
        if change_from_last_month < greatest_decrease:
            greatest_decrease = change_from_last_month
            decrease_month = csv_data[i][0]
average_price = amount/line_count

print('Total Months:', total_months)
print('Total Profit:', amount)    
print('Average Profit:', average_price)
print('Largest recorded Increase:', greatest_increase)
print('Largest recorded Decrease:', greatest_decrease)    
    


