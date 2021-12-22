# xlrd 读 excel
import xlrd

book = xlrd.open_workbook('data.xlsx')
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
print(u'表格总行数 ',nrows)
ncols = sheet1.ncols
print(u'表格总列数 ',ncols)
row3_values = sheet1.row_values(2)
print(u'第3行值 ',row3_values)
col3_values = sheet1.col_values(2)
print(u'第3列值 ',col3_values)
cell_3_3 = sheet1.cell(2,2).value
print(u'第3行第3列的单元格的值：',cell_3_3)

# xlwt 写 excel
import xlwt  # 不支持excel2007的xlsx格式

workbook = xlwt.Workbook()

worksheet = workbook.add_sheet('test')

worksheet.write(0,0,'A1data')

workbook.save('excelwrite.xls')
