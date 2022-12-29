# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 10:52:59 2022

@author: 沈纪中
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12.8,7.2),dpi=800)
df=pd.read_excel("实验数据.xlsx")
x=df['Time (s)']
y=df['Linear Acceleration z (m/s^2)']
plt.plot(x,y,label="Linear Acceleration z (m/s^2)")
plt.title("Linear Acceleration z (m/s^2)")
plt.xlabel("时间")
plt.ylabel("z轴加速度")
plt.legend()
plt.savefig('1.png')
plt.show()
