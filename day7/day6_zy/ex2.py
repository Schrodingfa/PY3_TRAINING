# Author:jxy
# 参照下列代码，定义根据月份返回天数的方法
# 要求：考虑2月，如果是闰年返回29天，否则返回28天
# mouth = int(input('please input a mouth:'))
#
# if mouth < 1 or mouth > 12:
#     print('invalid parameter')
# elif mouth == 2:
#     print('28')
# elif mouth in (1, 3, 5, 7, 8, 10, 12):
#     print('31')
# else:
#     print('30')
#
# day = 29 if not year % 4 and year % 100 or not year % 400 else 28

def day_of_month(year,month):
    if month < 1 or month > 12:
        return 'invalid parameter'
    elif month == 2:
        if not year % 4 and year % 100 or not year % 400:
            return 29
        else:
            return 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30

month = int(input('please input a month:'))
year = int(input('please input a year:'))
res = day_of_month(year,month)
print(res)