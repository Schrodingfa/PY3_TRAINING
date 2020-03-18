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
