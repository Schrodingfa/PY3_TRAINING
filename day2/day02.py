# Author:jxy

# a = 777
# b = 777
# print(id(a), id(b))
#
# del a, b
# c = 777
# print(id(c))

# print("10"+"2")
# print(bool(0.00))
#
# name = input("姓名:")
# sex = input("姓别:")
# age = int(input("年龄:"))
# score = float(input("成绩:"))
# print("我的姓名是%s，性别是%s，年龄是%d，成绩是%.1f" % (name, sex, age, score))

price = float(input("商品单价:"))
amount = int(input("商品数量:"))
money = int(input("支付金额:"))
result = money - price * amount

print("找零:"+str(result))
