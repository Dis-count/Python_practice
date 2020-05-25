from pyecharts.charts import Bar
from pyecharts import options as opts
# 柱状图反转
bar = Bar()
x = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
y = [820, 932, 901, 934, 1290, 1330, 1320]
bar.add_xaxis(list(x))
bar.add_yaxis("嘿嘿",y,itemstyle_opts=opts.ItemStyleOpts(color='green'))
bar.reversal_axis() # 反转
bar.render_notebook()
