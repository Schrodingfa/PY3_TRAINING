# 在控制台中获取一个年份，如果是闰年给变量day赋值29，平年赋值28

year = int(input("please input a year:"))
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# print(day)

day = 29 if not year % 4 and year % 100 or not year % 400 else 28
print(day)
