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