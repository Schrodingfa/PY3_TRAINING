"""
在控制台中获取一个月份
打印季节（春1--3 夏4--6 秋7--9 冬10--12）
"""

mouth = int(input('please input a mouth:'))
# if 1 <= mouth <= 3:
#     print('spring')
# elif 4 <= mouth <= 6:
#     print('summer')
# elif 7 <= mouth <= 9:
#     print('autumn')
# elif 10 <= mouth <= 12:
#     print('winter')
# else:
#     print('invalid parameter')

if mouth < 1 or mouth > 12:
    print('invalid parameter')
elif mouth <= 3:
    print('spring')
elif mouth <= 6:
    print('summer')
elif mouth <= 9:
    print('autumn')
else:
    print('winter')
