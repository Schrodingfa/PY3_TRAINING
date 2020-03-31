# Author:jxy
# 根据月份显示天数
t01 = (1,3,5,7,8,10,12)
t02 = (4,6,9,11)
t03 = (2,)

month = int(input("please input month:"))
if month in t01:
    print("31")
elif month in t02:
    print("30")
elif month in t03:
    print("28")

"""
在控制台中获取一个月份
打印该月有几天
"""

mouth = int(input('please input a mouth:'))

if mouth < 1 or mouth > 12:
    print('invalid parameter')
elif mouth == 2:
    print('28')
elif mouth in (1, 3, 5, 7, 8, 10, 12):
    print('31')
else:
    print('30')
