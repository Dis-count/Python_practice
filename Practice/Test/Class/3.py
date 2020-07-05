# 根据NVDA的数据，设计交易策略，最大化回报率。欢迎大家下次课（周一）踊跃分享

# NVDA 384.49 3.29 0.86% : NVIDIA Corporation - Yahoo Finance
# https://finance.yahoo.com/quote/NVDA?p=NVDA

import pandas as pd
import numpy as np

df = pd.read_csv('santaclara_sfh.csv')
# make the date column of type datetime
df['date'] = pd.to_datetime(df.date)
# make the price column of type float
df['median_sfh_price_past_3_months'] = \
    df.median_sfh_price_past_3_months + 0.0
# make data the index ////inplace cover the original one
df.set_index('date',inplace = True)
# take the series of median prices
housing = df['median_sfh_price_past_3_months']
housing.name = 'housing'

df

housing.plot()


data = pd.read_csv('GOOGL.csv', index_col =0, parse_dates =True)
# 第一列作为 index

stock = data['Close']

# to align the two series
# step1 : pad stock so that there are no missing days
stock.head(10)

padded = stock.asfreq(freq = '1D', method = 'ffill') #填充股票数据用于补齐 forward / backward fill
padded.head(20)
# step2 : compute the 90-day moving median of stock

movmed = padded.rolling(90).median()

movmed[80:120]
# step 3: retain the same days as in the housing series.
# only retain the final day of every month.

housing.index

mod_stock = movmed[housing.index]

mod_stock.head(10)

# compute correlation

housing.corr(mod_stock)

import matplotlib.pyplot as plt

plt.plot(mod_stock, 'b')
plt.plot(housing, 'r')

norm_stock = mod_stock/mod_stock[0]

norm_housing = housing/housing.iloc[0]

plt.plot(norm_stock, 'b')
plt.plot(norm_housing, 'r')

plt.legend(['Stock','Housing'])
