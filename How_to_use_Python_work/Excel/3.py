# pandas read excel
import pandas as pd

df = pd.read_excel(r'data.xlsx',sheetname=0)

print(df)

# encoding: utf-8
from pandas import DataFrame

data={
'name':[u'张三',u'李四',u'王五'],
'age':[21,22,23],
'sex':[u'男',u'女',u'男']
}
df = DataFrame(data)
df.to_excel('new.xlsx')
