import os
import csv

Total_Months=[]
Profit_Sum=[]
Earnings_Total=0
Change=[]
Average_Total=0

# Path to collect data from the Resources folder
budget = os.path.join('Resources','budget_data.csv')

with open(budget) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:      
        
        Date=row[0]
        Earnings= row[1]
        Total_Months.append(Date)
        Profit_Sum.append(Earnings)
        Change.append(Earnings)
        

print(f'Financial Analysis')
print(f'------------------------')

Months=len(Total_Months)
print(f"Total Months: " + str(Months))

#determine Earnings_Total
for i in range(0,len(Profit_Sum)):
    Earnings_Total=Earnings_Total+int(Profit_Sum[i])
print(f'Total: ${Earnings_Total}')    

#determine average change
Change=[float(Profit_Sum[i+1])-float(Profit_Sum[i]) for i in range(len(Profit_Sum)-1)]
Average_Total=sum(Change)/int(len(Change))

print(f'Average Change: ${Average_Total}')

#max/min of Change list
max_change=max(Change)
max_index=(Change.index(max_change)+1)
max_date=Total_Months[max_index]
min_change=min(Change)
min_index=(Change.index(min_change)+1)
min_date=Total_Months[min_index]
print(f'Greatest Increase in Profits: {max_date} (${max_change})')
print(f'Greatest Decrease in Profits: {min_date} (${min_change})')

# Specify the file to write to
output = os.path.join("analysis", "budget_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow([f'Total Months: ' + str(Months)])
    csvwriter.writerow([f'Total: ${Earnings_Total}'])
    csvwriter.writerow([f'Average Change: ${Average_Total}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {max_date} (${max_change})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {min_date} (${min_change})'])
    
