# 线下数据

from impala.dbapi import connect
from impala.util import as_pandas
import datetime

conn = connect(host='host',port=21050,auth_mechanism='PLAIN',user='user',password='password')
#host：数据库域名
#user：数据库用户名
#password：数据库密码
df_data = pd.read_excel('temp.xlsx')

rows =[]
for index, row in df_data.iterrows():
    rows.append('('+'"'+str(row['case_id']).replace('nan','null')+'"'+','+'"'+str(row['birth_date'])+'"'+')'+',')
    a= '''
    INSERT into table
    (case_id, birth_date)
    values '''
for i in rows:
    a += i
a = a[:-1]

cursor1 = conn.cursor()
cursor1.execute(a)
cursor1.close()
conn.close()
print('成功导入数据至数据库...')
del a
del rows

# 线上数据

import sql   #sql是封装的sql文件
sql_end = sql.sql_end
cursor1 = conn.cursor()
for i in sql_end.split(';'):
    print(i)
    cursor1.execute(i)
cursor1.close()
conn.close()
print('程序运行结束，请执行下一步。')
