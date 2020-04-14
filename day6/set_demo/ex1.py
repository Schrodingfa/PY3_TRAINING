# 在控制台中随意录入多个字符串
# 按q退出，再显示所有不重复的字符串
set1 = set()
while True:
    str1 = input("please input a string:")
    if str1 == "q":
        break
#    else:
    for i in str1:
        set1.add(i)


print(set1)
