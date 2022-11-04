'''
weight=float(input("请输入你的体重："))
hight=float(input("请输入你的升高："))
BMI=weight/hight**2
if BMI<18.5:
    a="，你偏瘦了。"
elif 18.5<=BMI<=23.9:
    a=",你体重正常。"
elif BMI>=23.9:
    a="，你偏胖了。"
BMI=str(round(BMI,2))
print("你的BMI是："+BMI+a)
'''
weight=float(input("请输入你的体重："))
hight=float(input("请输入你的升高："))
BMI=weight/hight**2
if BMI<18.5:
    a="，你偏瘦了。"
elif 18.5<=BMI<=23.9:
    a=",你体重正常。"
elif BMI>=23.9:
    a="，你偏胖了。"
BMI=round(BMI,2)
print("你的BMI是：",BMI,a)
