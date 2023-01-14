import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image
from nltk.probability import FreqDist
#停用词列表：不显示在词云上
STOPWORDS=['的',',','，','了','是','在','和','曰',' ','。','：','“','”','之','不',\
           '\n', '、','？','；','！',' ']
#读入背景图片
abel_mask = np.array(Image.open("love.png"))
#读取要生成词云的文件
texts= open('words.txt',encoding='utf-8').read()
#通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(texts,cut_all = False)
wl_space_split = " ".join(wordlist_after_jieba)
cut_txt=wl_space_split
#词频统计
def showInfo(cut_text):
    fdist=FreqDist(cut_text)
    return fdist
fdist=showInfo(cut_txt) 
tops=fdist.most_common(20) 
cut_txt=[word for word in cut_txt if word not in STOPWORDS]#利用列表推导式去除停用词
fdist=showInfo(cut_txt) 
tops=fdist.most_common(20) 
print (tops)
#构建词云
my_wordcloud = WordCloud(
            background_color='white',    # 设置背景颜色
            mask = abel_mask, # 设置背景图片
            max_words = 200, # 设置最大显示的字数
            stopwords =STOPWORDS, # 设置停用词
            scale=2,        # 比列放大  数值越大  词云越清晰
            font_path = 'C:/Users/Windows/fonts/simkai.ttf',# 设置字体格式，如不设置显示不了中文
            max_font_size = 80, # 设置字体最大值
            ).generate(wl_space_split)
# 以下代码显示图片
image=my_wordcloud.to_image()
out = image.resize(Image.ANTIALIAS)
image.show()
image.to_file('1.png')