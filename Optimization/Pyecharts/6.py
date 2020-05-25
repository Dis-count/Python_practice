from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType,SymbolType

g1 = Geo()
g1.add_schema(maptype='河南')
g1.add('geo',[['郑州',20],['新乡',30],['许昌',2800]])
g1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
g1.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=3000), # 显示左下角颜色控制
                  title_opts=opts.TitleOpts(title='示例'))

g1.render_notebook()
