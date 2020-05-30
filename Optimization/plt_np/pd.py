from pandas import DataFrame

data={
'name':[u'张三',u'李四',u'王五'],
'age':[21,22,23],
'sex':[u'男',u'女',u'男']
}
df = DataFrame(data)
df.to_excel('./Data/new.xlsx')


from pandas import DataFrame
data = DataFrame(np.arange(16).reshape(4,4),index = list("ABCD"),columns=list('wxyz'))

data.to_excel(r'F:\pypractice\Yun\doc\2.xls', sheet_name='Sheet1')        #将dataframe形式的数据框存储到Excel文件中



writer = pd.ExcelWriter(r'C:\Users\mapping.xlsx')
df = pd.concat(li)
df.to_excel(writer,'Sheet1',index=False,header = None)
df
