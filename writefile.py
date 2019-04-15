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
writer.save()





