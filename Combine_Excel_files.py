import os
import pandas as pd
#set src directory
os.chdir('put src directory')
def read_sheets(files):
    result = []
    for filename in files:
        sheets = pd.read_excel(filename, sheet_name=None)
        for name, sheet in sheets.items():
            sheet['Sheetname'] = name
            sheet['Row'] = sheet.index
            result.append(sheet)
    return pd.concat(result, ignore_index=True)
folder_path = '.'
files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")] 
dfCombined = read_sheets(files)
writer = pd.ExcelWriter('Master_excel_file.xlsx')
dfCombined.to_excel(writer, index=None, sheet_name='Combined')
writer.save()
writer.close()