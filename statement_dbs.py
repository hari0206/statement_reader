import xlrd


workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\Banking\dbsstatement.xls')
workbook = xlrd.open_workbook(r'C:\Users\lenovo\Desktop\Banking\dbsstatement.xls', on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = []
for col in range(worksheet.ncols):
    for sheet in workbook.sheets():
        for rowidx in range(sheet.nrows):
            row = sheet.row(rowidx)
            for colidx, cell in enumerate(row):
                if cell.value == "Date" :
                    first_row.append( worksheet.cell_value(rowidx,col) )
data =[]
for sheet in workbook.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        for colidx, cell in enumerate(row):
            if cell.value == "Date" :
                for row in range(rowidx+1, worksheet.nrows):
                    elm = {}
                    for col in range(worksheet.ncols):
                        elm[first_row[col]]=worksheet.cell_value(row,col)
                    data.append(elm)          
for x in data:
    for y in data:
        if x['Date']=='':
            res = {key: x[key] + y.get(key, '') for key in x.keys()}
for x in data:
    if x['Date'] == '':
        data.remove(x)  
for x in data:
    x.pop('')

print(data, len(data))