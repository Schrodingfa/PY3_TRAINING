# Author:jxy
# 在控制台中获取一个字符串
# 1.打印最后一个字符
# 2.打印第一个字符
# 3.如果是奇数，打印中间的字符串
# 4.打印倒数三个字符
# 5.倒叙打印字符串

str = input("please input a string:")
# 1
print(str[-1])
print(str[len(str) - 1])
# 2
print(str[0])
print(str[-len(str)])
# 3
if len(str) % 2 == 1:
    print(str[len(str) // 2])
# 4
print(str[-3:])

# 5
print(str[::-1])
