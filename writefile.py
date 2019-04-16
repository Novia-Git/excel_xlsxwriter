import pandas as pd

#Your data
df = pd.DataFrame( {'Item':['Food','Clothing','Housing','Transportation'], 'Cost':[6000,3000,10000,5000]})
#Use xlsxwriter
writer = pd.ExcelWriter('Livecost.xlsx',engine='xlsxwriter')  
#Write to an excel file
df.to_excel(writer,sheet_name='Sheet1')
#Load
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
row=0
for item, cost in df.iterrows():
    row += 1
#Write data
worksheet.write('B6', 'Total:')
worksheet.write(row+1, 2, '=SUM(C2:C5)')
#Create a chart
chart = workbook.add_chart({'type': 'column'})
#Configure the data to add series
chart.add_series({'values': '=Sheet1!$C$2:$C$5'})
#Insert the chart 
worksheet.insert_chart('E2', chart)
#Close file
writer.save()





