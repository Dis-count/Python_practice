# -*- coding: utf-8 -*-

#将多个Excel文件合并成一个
import xlrd
import xlsxwriter

#获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()

#获取sheet表的行数
def getnrows(fh,sheet):
    table = fh.sheets()[sheet]
    return table.nrows

#读取文件内容并返回行内容
def getFilect(file,shnum):
    fh = open_xls(file)
    table = fh.sheets()[shnum]
    num = table.nrows
    for row in range(num):
        rdata = table.row_values(row)
        datavalue.append(rdata)
    return datavalue
--------------------------------------
# 或者直接用concat+一个循环来实现：
for i in var_list:
    df_0 = data[['var_1','var_2','var_3','var_4',i]][data[i]=='信息']
    df_0['month'] = date_replace(i)
    df_0 = df_0[['var_1','var_2','var_3','var_4','var_5']]
    li.append(df_0)

writer = pd.ExcelWriter(r'C:\Users\mapping.xlsx')
df = pd.concat(li)
df.to_excel(writer,'Sheet1',index=False,header = None)
df
