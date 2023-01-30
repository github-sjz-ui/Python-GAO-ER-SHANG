# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:11:09 2023

@author: 15459
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12.8,7.2),dpi=800)
df=pd.read_excel("杭州电梯.xlsx")
x=df['Time (s)']
y=df['Linear Acceleration z (m/s^2)']
data_x = x
data_y = y

# 绘制曲线
plt.figure(figsize=(12.8,7.2),dpi=800)
poly = np.polyfit(data_x, data_y, deg=100)
y_value = np.polyval(poly, data_x)
plt.plot(data_x, y_value)
plt.title("Linear Acceleration z (m/s^2)")
plt.xlabel("时间")
plt.ylabel("z轴加速度")
plt.show()