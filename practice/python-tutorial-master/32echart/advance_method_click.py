# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""
from __future__ import unicode_literals


from pyecharts_javascripthon.dom import alert

import pyecharts.echarts.events as events
from pyecharts import Map

def on_click(params):
    alert(params.name)
    print(params.name)


def test_map_show_label():
    # show label
    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    map = Map("全国地图示例", width=1200, height=600)
    map.add("", attr, value, maptype="china", is_label_show=True)
    map.on(events.MOUSE_CLICK, on_click)
    map.render("click_map.html")


test_map_show_label()