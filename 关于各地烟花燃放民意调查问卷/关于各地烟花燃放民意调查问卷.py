import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12.8,7.2),dpi=800)
df1=pd.read_excel("关于各地烟花燃放民意调查问卷.xlsx")
df2=df1['2、你知道你所在地区对烟花燃放是如何规定吗？']
labels = 'A', 'B', 'C' # 定义标签
a=df2[df2.str.contains("A")].count()
b=df2[df2.str.contains("B")].count()
c=df2[df2.str.contains("C")].count()
sizes = [a/(a+b+c), b/(a+b+c),c/(a+b+c)]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue']  # 每一块的颜色
explode = (0, 0.1, 0)  # 突出显示，这里仅仅突出显示第二块（即'Hogs'）
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.show()