import xlrd, re, json

workbook = xlrd.open_workbook('hdfcstatement.xls')
workbook = xlrd.open_workbook('hdfcstatement.xls', on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = []
for col in range(worksheet.ncols):
    for sheet in workbook.sheets():
        for rowidx in range(sheet.nrows):
            row = sheet.row(rowidx)
            for colidx, cell in enumerate(row):
                if cell.value == "Date" :
                    first_row.append( worksheet.cell_value(rowidx,col) )
data_preview =[]
for sheet in workbook.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == "Date" :
                for row in range(rowidx+1, worksheet.nrows):
                    elm = {}
                    for col in range(worksheet.ncols):
                        elm[first_row[col]]=worksheet.cell_value(row,col)
                    data_preview.append(elm) 
data=[]
for x in data_preview:
    check = re.search(r'(\d+/\d+/\d+)', str(x['Date']))
    if check:
        data.append(x)
        
with open('result_hdfc.json', 'w') as f:
    json.dump(data, f)
print(data, len(data))