"""
在控制台中获取一个季度
打印月份
"""

season = int(input('please input a season:'))

if season < 1 or season > 4:
    print('invalid parameter')
elif season == 1:
    print('1 2 3')
elif season == 2:
    print('4 5 6')
elif season == 3:
    print('7 8 9')
else:
    print('10 11 12')
