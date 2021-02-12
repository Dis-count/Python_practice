# google 股票价格 和 湾区房屋价格

# Univariate time series

## print all the outputs in a cell
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

import pandas as pd
import numpy as np

data = pd.read_csv('GOOGL.csv', index_col =0, parse_dates =True)
# 第一列作为 index
data.head()

data.tail()

stock = data['Close']

stock.describe()

stock.index

stock.values

%pylab inline
stock.plot()

# exploring a time series

stock.head(10)

stock.tail()

stock.index[:10]

len(stock)

stock.nlargest(1)

stock.nlargest(10)

(stock.values[-1] - stock.values[0])/stock.values[0]

# moving average
rol = stock.rolling(50)

type(rol)

stock[:50].mean()

rol.mean()

pd.set_option('display.max_rows',100)

rol.mean().head(100)

stock.head()

stock.shift(1)
stock.shift(-1)

# 5 days later
futureprice = stock.shift(-5)

profits = (futureprice-stock)/stock

profits.mean()
# expected profits

profits.describe()

100 * profits.mean()* len(stock-5)

# the 20-day moving average strategy
profits

movavg = stock.rolling(20).mean()

stock > movavg

profits[stock > movavg].mean()

len(profits[stock > movavg])


#strategy: 买入卖出规则  20均线 附近上下买入卖出
