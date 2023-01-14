import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #中文显示
plt.rcParams['axes.unicode_minus'] = False
df1=pd.read_excel("关于各地烟花燃放民意调查问卷.xlsx")
df2=df1['2、你知道你所在地区对烟花燃放是如何规定吗？']
labels = 'A.知道', 'B.好像知道，听说过但不太清楚', 'C.一点都不知道' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
sizes = [a/(a+b+c), b/(a+b+c),c/(a+b+c)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue']  # 每一块的颜色
explode = (0, 0.1, 0.2)  # 突出显示
title="2、你知道你所在地区对烟花燃放是如何规定吗？"
plt.figure(figsize=(10,8),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()  # 添加上这一行，画完第一个图后，重置一下
df2=df1['3、如果你所在地禁止燃放烟花，你会认可并遵守这项规定吗?']
labels = 'A.遵守并认可 ', 'B.不太认可,大部分时候遵守,有时候忍不住会放烟花 ', 'C.不认可也不会遵守 ','D.不认可但会遵守规定' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
d=df2[df2.str.contains("D")].count()#统计选D的人数
sizes = [a/(a+b+c+d), b/(a+b+c+d),c/(a+b+c+d),d/(a+b+c+d)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue','aquamarine']  # 每一块的颜色
explode = (0, 0.1, 0.2,0.15)  # 突出显示
title="3、如果你所在地禁止燃放烟花，你会认可并遵守这项规定吗?"
plt.figure(figsize=(12.8,7.2),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()
df2=df1['4、你平时会燃放烟花吗？']
labels = 'A.不会，因为禁止燃放，严格遵守', 'B.会，虽然禁止燃放，但会偷偷放', 'C.会，允许燃放','D.不会，尽管允许燃放，但也不会放烟花' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
d=df2[df2.str.contains("D")].count()#统计选D的人数
sizes = [a/(a+b+c+d), b/(a+b+c+d),c/(a+b+c+d),d/(a+b+c+d)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue','aquamarine']  # 每一块的颜色
explode = (0, 0.1, 0.15,0.1)  # 突出显示
title="4、你平时会燃放烟花吗？"
plt.figure(figsize=(12.8,7.2),dpi=300)
plt.pie(sizes, explode=explode,labels=labels,colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()
df2=df1['5、对于烟花你的看法是？']
labels = 'A.喜欢看喜欢放', 'B.喜欢看不喜欢放', 'C.不喜欢看喜欢放','D.不喜欢看也不喜欢放' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
d=df2[df2.str.contains("D")].count()#统计选D的人数
sizes = [a/(a+b+c+d), b/(a+b+c+d),c/(a+b+c+d),d/(a+b+c+d)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue','aquamarine']  # 每一块的颜色
explode = (0, 0.1, 0.125,0.15)  # 突出显示
title="5、对于烟花你的看法是？"
plt.figure(figsize=(12.8,7.2),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()
df2=df1['6、你认为烟花爆竹的声音会影响到你的日常生活吗?']
labels = 'A.不会影响', 'B.有一点影响', 'C.有较大影响，总是被打扰','D.其他' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
d=df2[df2.str.contains("D")].count()#统计选D的人数
sizes = [a/(a+b+c+d), b/(a+b+c+d),c/(a+b+c+d),d/(a+b+c+d)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue','aquamarine']  # 每一块的颜色
explode = (0.05, 0.1, 0.125,0.15)  # 突出显示
title="6、你认为烟花爆竹的声音会影响到你的日常生活吗?"
plt.figure(figsize=(12.8,7.2),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()
df2=df1['7、你对当地烟花燃放相关工作开展的是否满意']
labels = 'A.满意', 'B.不满意' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
sizes = [a/(a+b), b/(a+b)]  # 每一块的比例
colors = ['yellowgreen', 'gold']  # 每一块的颜色
explode = (0.05, 0.1)  # 突出显示
title="7、你对当地烟花燃放相关工作开展的是否满意"
plt.figure(figsize=(10,8),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()
df2=df1['8、你觉得禁燃烟花利大于弊还是弊大于利?']
labels = 'A.利＞弊', 'B.利＜弊', 'C.无所谓，不关我的事' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
sizes = [a/(a+b+c), b/(a+b+c),c/(a+b+c)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue']  # 每一块的颜色
explode = (0.05, 0.1, 0.2)  # 突出显示
title="8、你觉得禁燃烟花利大于弊还是弊大于利?"
plt.figure(figsize=(12.8,7.2),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
plt.clf()
df2=df1['9、你是否支持燃放烟花爆竹？']
labels = 'A.支持', 'B.不支持', 'C.无所谓' # 定义标签
a=df2[df2.str.contains("A")].count()#统计选A的人数
b=df2[df2.str.contains("B")].count()#统计选B的人数
c=df2[df2.str.contains("C")].count()#统计选C的人数
sizes = [a/(a+b+c), b/(a+b+c),c/(a+b+c)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue']  # 每一块的颜色
explode = (0.05, 0.1, 0.2)  # 突出显示
title="9、你是否支持燃放烟花爆竹？"
plt.figure(figsize=(12.8,7.2),dpi=300)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.legend(title=title)
plt.show()
