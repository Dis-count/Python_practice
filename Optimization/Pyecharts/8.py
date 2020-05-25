# 手动添加经纬度 自定义左下角单位
from pyecharts.globals import GeoType,ChartType
city = '杭州'
g3 = Geo()
g3.add_schema(maptype=city,is_roam=False)

# 手动添加经纬度
g3.add_coordinate('杭州师范',120.12321,30.2143432)
g3.add_coordinate('不懂大学',120.2712434,30.16233434)

data_pair = [['杭州师范',100],['不懂大学',500],['杭州',50]]
g3.add(' ',data_pair,symbol_size=20,type_=GeoType.EFFECT_SCATTER) # 涟漪效果 热图：ChartType.HEATMAP

# 左下角自定义
pieces = [
    {'max':6,'label':'5一下','color':'pink'},
    {'min':6,'max':10,'label':'5-10','color':'red'},
    {'min':10,'max':100,'label':'10-100','color':'blue'}
]

g3.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=True,pieces=pieces),#,max_=800 # 显示左下角颜色控制
                  title_opts=opts.TitleOpts(title='示例嘿嘿'))

g3.render_notebook()
