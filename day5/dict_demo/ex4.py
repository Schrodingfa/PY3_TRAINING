"""
在控制台中获取一个季度
打印月份
"""
season_dict = {1: "1 2 3", 2: "4 5 6", 3: "7 8 9", 4: "10 11 12"}
season = int(input('please input a season:'))

# if season < 1 or season > 4:
if season not in season_dict:
    print('invalid parameter')
else:
    print(season_dict[season])
