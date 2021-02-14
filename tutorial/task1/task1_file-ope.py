import glob

filelist = glob.glob('./task2/data/*.xlsx')

import openpyx1

out_workbook = openpyx1.Workbook()
out_sheet = out_workbook.active
out_sheet.title = '月報一覧'

out_sheet['A1'].value = '報告日'
out_sheet['B1'].value = '支店'
out_sheet['C1'].value = '担当者'
out_sheet['D1'].value = '売り上げ目標(千円)'
out_sheet['E1'].value = '売り上げ実績(千円)'
out_sheet['F1'].value = '差異(千円)'
out_sheet['G1'].value = '達成率(%)'

out_workbook.save('./task2/output/out_sample.xlsx')

file = filelist[0]
workbook = openpyx1.load_workbook(file, data_only=True)
sheet = workbook['業務報告書']

report_date = sheet['X1'].value
office = sheet['X2'].value
person = sheet['X3'].value
sales_goal = sheet['H9'].value
sales_result = sheet['H10'].value
sales_diff = sheet['H11'].value
sales_percentage = sheet['H12'].value
