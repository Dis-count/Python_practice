# Page
from pyecharts.charts import Line,Page
from pyecharts import options as opts
f1 = Line()
f1.add_xaxis(list(x))
f1.add_yaxis('aa',y,is_smooth=True)
f1.set_global_opts(title_opts=opts.TitleOpts('哈哈哈'),
                   datazoom_opts=opts.DataZoomOpts(is_show=True), # 缩放
                  xaxis_opts=opts.AxisOpts(type_='value')) # 类型 ：categary / value
f1.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
f1.render_notebook()

f2 = Line()
f2.add_xaxis(list(x))
f2.add_yaxis('aa',y,is_smooth=True)
f2.set_global_opts(title_opts=opts.TitleOpts('哈哈2哈'),
                   datazoom_opts=opts.DataZoomOpts(is_show=True), # 缩放
                  xaxis_opts=opts.AxisOpts(type_='value')) # 类型 ：categary / value
f2.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
f2.render_notebook()

page = Page(layout=Page.DraggablePageLayout)
page.add(f1,f2)
page.render()

# 保存成固定html
# page.save_resize_html('./render.html',cfg_file='./chart_config.json',dest='./new.html')
