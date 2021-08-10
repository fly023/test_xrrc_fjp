# -*- encoding: utf-8 -*-
# Project: q1.py
# __author__ = 'fangjp'

import pandas as pd
from pyquery import PyQuery as pq

with open('baidu.html', encoding="UTF-8") as f:
    f = f.read()
    doc = pq(f)
    new_df = pd.DataFrame(columns=['地区', '新增', '现有', '累计', '治愈', '死亡'])
    n = 0
    for value in doc('.VirusTable_1-1-312_3m6Ybq').items():
        n += 1
        city = value('.VirusTable_1-1-312_MdE8uT span').eq(1).text()
        new = value('.VirusTable_1-1-312_3x1sDV.VirusTable_1-1-312_2bK5NN').text()
        now = value('.VirusTable_1-1-312_3x1sDV').eq(0).text()
        all = value('.VirusTable_1-1-312_3x1sDV').eq(1).text()
        suc = value('.VirusTable_1-1-312_EjGi8c').eq(0).text()
        die = value('.VirusTable_1-1-312_EjGi8c').eq(1).text()
        new_df.loc[n, '地区'] = city
        new_df.loc[n, '新增'] = new
        new_df.loc[n, '现有'] = now
        new_df.loc[n, '累计'] = all
        new_df.loc[n, '治愈'] = suc
        new_df.loc[n, '死亡'] = die
        print(city, new, now, all, suc, die)
    new_df.to_csv('./国内各地区疫情汇总.csv')
