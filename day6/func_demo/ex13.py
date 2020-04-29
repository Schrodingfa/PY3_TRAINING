# Author:jxy
# day3 ex1 升级版
# 定义根据月份判断季节的方法

def season(month):
    if month < 1 or month > 12:
        return 'invalid parameter'
    if month <= 3:
        return 'spring'
    if month <= 6:
        return 'summer'
    if month <= 9:
        return 'autumn'
    return 'winter'

m = int(input('please input a mouth:'))

res = season(m)
print(res)

