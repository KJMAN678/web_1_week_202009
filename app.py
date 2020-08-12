# 【Streamlit】JavaScriptが嫌いだからPythonだけでWebアプリをつくる より
# https://qiita.com/SPShota/items/a63e19807779175aa29b

import streamlit as st
import pandas as pd
import requests

@st.cache
def get_covid_df(url):
    response_json = requests.get(url).json()
    df = pd.DataFrame(response_json['data'])
    return df

url = 'https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/development/data/daily_positive_detail.json'
df_covid = get_covid_df(url)

"""
# 東京都のCOVID-19感染者数
東京都 新型コロナウイルス感染症対策サイトの[Github](https://github.com/tokyo-metropolitan-gov/covid19)からデータを取得
"""

st.write(df_covid)


# part_2

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""
# 日毎の感染者数
"""


x = [
    datetime.datetime.strptime(diagnosed_date, '%Y-%m-%d')
    for diagnosed_date in df_covid['diagnosed_date'].values
]
y_count = df_covid['count'].values

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y_count)

xfmt = mdates.DateFormatter('%m/%d')
xloc = mdates.DayLocator(interval=20)

ax.xaxis.set_major_locator(xloc)
ax.xaxis.set_major_formatter(xfmt)
st.write(fig)