# 在控制台输入月、日，计算这是一年中的第几天

month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
r = 0
month = int(input("please input the month:"))
day = int(input("please input the day:"))
if month < 1 or month > 12:
    print('invalid parameter')
elif day < 1 or day > month_tuple[month - 1]:
    print('invalid parameter')
else:
    # for i in range(month - 1):
    #     r += month_tuple[i]
    # 利用聚合函数以及切片求和
    r = sum(month_tuple[:month-1])
    r += day
    print(r)

