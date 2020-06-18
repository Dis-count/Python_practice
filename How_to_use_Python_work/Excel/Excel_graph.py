import xlsxwriter

#设置一个例子
data = [20, 45, 26, 18, 45]

#创建表格
workbook = xlsxwriter.Workbook("temp.xlsx")
worksheet = workbook.add_worksheet("data")

#添加数据
worksheet.write_column('A1', data)

#创建图表
chart = workbook.add_chart({'type': 'line'})

#图表添加数据
chart.add_series({
        'values': '=data!$A1:$A6',
        'name': '图表名称',
        'marker': {
                'type': 'circle',
                'size': 8,
                'border': {'color': 'black'},
                'fill': {'color': 'red'}
                } ,
        'data_labels': {'values': True},
        'trendline': {
                'type': 'polynomial',
                'order': 2,
                'name': '趋势线',
                'forward': 0.5,
                'backward': 0.5,
                'display_equation':True,
                'line': {'color': 'red', 'width':1, 'dash_type': 'long_dash'}
                }
})

worksheet.insert_chart('c1', chart)
workbook.close()
