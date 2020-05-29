import xlrd
import xlwr
# 打开excel
readbook = xlrd.open_workbook(r'\test\canying.xlsx')
# 获取读入文件的sheet
sheet = readbook.sheet_by_index(1) #索引的方式，从0开始
sheet = readbook.sheet_by_name('sheet2')#名字的方式
# 获取sheet的最大行数和列数
nrows = sheet.nrows#行
ncols = sheet.ncols#列
# 获取某个单元格的值
lng = table.cell(i,3).value #获取i行3列的表格值
lat = table.cell(i,4).value #获取i行4列的表格值
# 打开将写的表并添加sheet
writebook = xlwt.Workbook()#打开一个excel
sheet = writebook.add_sheet('test')#在打开的excel中添加一个sheet
# 将数据写入excel
sheet.write(i,0,result[0])#写入excel，i行0列
sheet.write(i,1,result[1])
# 保存
writebook.save('answer.xls') #一定要记得保存
