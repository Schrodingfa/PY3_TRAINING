# Author:jxy

target = int(input("please input a number:"))

second = target % 60
minute = target // 60 % 60
hour = target // 3600


print(str(hour)+" hours "+str(minute)+" minutes "+str(second)+" seconds.")



