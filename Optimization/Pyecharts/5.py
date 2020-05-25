#地图Geo
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType,SymbolType

go = Geo()
go.add_schema(maptype='china')
go.add('geo',[list(i) for i in zip(Faker.provinces,Faker.values())])
go.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
go.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True), # 显示左下角颜色控制
                  title_opts=opts.TitleOpts(title='示例'))

go.render_notebook()
