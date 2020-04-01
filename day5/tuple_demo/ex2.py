# Author:jxy
# 根据月份显示天数
# t01 = (1,3,5,7,8,10,12)
# t02 = (4,6,9,11)
# t03 = (2,)
#
# month = int(input("please input month:"))
# if month in t01:
#     print("31")
# elif month in t02:
#     print("30")
# elif month in t03:
#     print("28")

# month = int(input('please input a month:'))
#
# if month < 1 or month > 12:
#     print('invalid parameter')
# elif month == 2:
#     print('28')
# elif month in (4, 6, 9, 11):
#     print('30')
# else:
#     print('31')

# 将每月的天数存入元组
month_tuple = (31,28,31,30,31,30,31,31,30,31,30,31)
month = int(input('please input a month:'))
if month < 1 or month > 12:
    print('invalid parameter')
else:
    print(month_tuple[month - 1])
