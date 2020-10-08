# import xlrd

# excle = xlrd.open_workbook("test.xlsx")
# table = excle.sheet_by_name("Sheet1")
# # value = table.row_values(1)
# x = table.nrows
# y = table.ncols
for i in range(1,10):
    print("------------------------------------------------------")
    rowlist = table.row_values(i)
    for j in rowlist:
        print(j,end="|")
    print ("")