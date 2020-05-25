# 柱状图
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()

bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.reversal_axis() # 反转
bar.render_notebook()

# Map与Geo的区别 Map可以是区域加颜色并显示名称
from pyecharts.charts import Map

g4 = Map()
# g4.add('嘿嘿',[list(z) for z in zip(Faker.provinces,Faker.values())],'china')
g4.add('嘿嘿',[['昌平区',200],['西城区',130],['海淀区',120],['通州区',133]],'北京')

g4.set_global_opts(title_opts=opts.TitleOpts(title='地图'),
                  visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=300))
g4.render_notebook()

# 隐藏Label
from pyecharts.charts import Map

g5 = Map()
# g4.add('嘿嘿',[list(z) for z in zip(Faker.provinces,Faker.values())],'china')
g5.add('北京',[['昌平区',200],['西城区',130],['海淀区',120],['通州区',133]],'北京',is_map_symbol_show=False) #is_map_symbol_show不出现点

g5.set_global_opts(title_opts=opts.TitleOpts(title='地图'),
                  visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=300))
g5.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) # label_opts隐藏Label, is_show=True
g5.render_notebook()

# 定位地图
from pyecharts.charts import BMap
from pyecharts.globals import ChartType,SymbolType


ak = 'fCWuW7dfaNQkpfx4VRWl46j5zyWlFjpa'
b1 = BMap()
b1.add_schema(baidu_ak=ak,center=[120.132343242,30.243242342],zoom=9) #zoom=10放大初始点

b1.add('bmap',
       [list(i) for i in zip(Faker.provinces,Faker.values())],
      label_opts=opts.LabelOpts(formatter={'b'}))

b1.set_global_opts(title_opts=opts.TitleOpts('BMap-示例'),
                  visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=2000,pos_bottom=60)) # 防止百度图标挡住
b1.render_notebook()
