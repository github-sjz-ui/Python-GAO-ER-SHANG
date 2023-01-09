'''
（选做）程序设计：
输入 5 位评委对 3 个作品的评分数据(评委对作品的评分数据由 3 位十进制数组成，第 1 位对应作品编号，
第 2、3 位对应作品得分， 分值范围为[60,99]。如“275”表示 2 号作品得分为 75 分)。程序输出 3 个作品的平均分和最高分的
作品编号。 
程序运行示例： 
输入：180/283/385/170/276/384/180/285/380/190/295/390/170/272/370
输出：作品 1 平均分为:78.0 作品 2 平均分为:82.2 作品 3 平均分为:81.8 得分最高的是作品2
'''
list1=input('输入评分').split('/')
sum_1=0
sum_2=0
sum_3=0
for i in list1:
    zp=i[0]#取出作品
    pf=int(i[1:])#取出评分
    if not 60<=pf<=99: 
        print('输入有误')
        break 
    if zp =='1':
        sum_1+=pf
    elif zp == '2':
        sum_2+=pf
    else:
        sum_3+=pf
aver_1=sum_1/5
aver_2=sum_2/5
aver_3=sum_3/5
list2=[aver_1,aver_2,aver_3]
aver_max=max(list2)
aver_max=list2.index(aver_max)+1
print('作品 1 平均分为:'+str(aver_1)+' 作品 2 平均分为:'+str(aver_2)+' 作品 3 平均分为:'+str(aver_3)+' 得分最高的是作品'+str(aver_max))
