# Author:jxy
# 在控制台中录入一个字符串
# 打印这个字符串中的字符以及出现的次数
# abcdbcd
# a 1
# b 2
# d 2
# c 2

d01 = {}
string = input("plesas input a string:")
for i in string:
    if i not in d01:
         d01[i] = 1
    else:
        d01[i] += 1

for k,v in d01.items():
    print(k+"\t"+str(v))
