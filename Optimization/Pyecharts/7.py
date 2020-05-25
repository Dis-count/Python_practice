from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType,SymbolType

g2 = Geo()
g2.add_schema(maptype='北京')
g2.add('北京',[['昌平',20],['西城',30],['海淀',20],['通州区',233]])
g2.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
g2.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=300), # 显示左下角颜色控制
                  title_opts=opts.TitleOpts(title='示例嘿嘿'))

g2.render_notebook()
