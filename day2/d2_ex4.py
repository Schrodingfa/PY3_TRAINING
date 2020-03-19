# Author:jxy

year = int(input("please enter the year:"))
result = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(result)

