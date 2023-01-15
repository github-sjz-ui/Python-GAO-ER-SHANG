# 导入相关库
import matplotlib.pyplot as plt
import pandas as pd
import jieba
plt.rcParams["font.sans-serif"]=["SimHei"]
# 读取数据
text=open("words.txt",encoding="utf-8").read()
cutwords=jieba.lcut(text,cut_all=False)
stopwords=['一个','两个','的',',','，','了','是','在','和','曰',' ','。','：','“','”','之','不','\n',\
            '、','？','；','！',' ','不知','不是','我们','为了','认为','可能','很大']
counts={}
for word in cutwords:
    if len(word)!=1 and word not in stopwords:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
df=pd.DataFrame([counts]).T
df=df.reset_index()
df.columns=["词","次数"]
df=df.sort_values("次数",ascending=False)
df.to_excel("words.xlsx")