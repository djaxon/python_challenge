import os
import csv

Total_Months=[]
Profit_Sum=[]
Change_Profit=[]
Earnings_Total=0
Earnings_Change=0


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
        Change_Profit.append(Earnings)

print(f'Financial Analysis')
print(f'------------------------')

Months=len(Total_Months)

print(f"Total Months: " + str(Months))
for i in range(0,len(Profit_Sum)):
    Earnings_Total=Earnings_Total+int(Profit_Sum[i])
print(f'Total: ${Earnings_Total}')    






