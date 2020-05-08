# Author:jxy
# 参照下列代码，定义根据月份返回天数的方法
# 要求：考虑2月，如果是闰年返回29天，否则返回28天
# month = int(input('please input a month:'))
#
# if month < 1 or month > 12:
#     print('invalid parameter')
# elif month == 2:
#     print('28')
# elif month in (1, 3, 5, 7, 8, 10, 12):
#     print('31')
# else:
#     print('30')
#
# day = 29 if not year % 4 and year % 100 or not year % 400 else 28

# 向外返回的结果，类型应该统一
# def day_of_month(year, month):
#     if month < 1 or month > 12:
#         return -1
#     elif month == 2:
#         if not year % 4 and year % 100 or not year % 400:
#             return 29
#         else:
#             return 28
#     elif month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     else:
#         return 30

# 一个函数只实现一个功能
def is_leap_year(year):
    return not year % 4 and year % 100 or not year % 400

def day_of_month(year, month):
    if month < 1 or month > 12:
        return -1
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    return 30


res = day_of_month(2014, 24)
print(res)
