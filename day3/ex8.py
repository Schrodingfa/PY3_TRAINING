# Author:jxy

# 计算最大值
# # 思路：假设第一个变量是最大值，
# #       然后依次与后面的变量作比较，若有更大的值则替换假设值

num01 = 8
num02 = 6
num03 = 10
num04 = 5
maxnum = num01
if num02 > maxnum:
    maxnum = num02
if num03 > maxnum:
    maxnum = num03
if num04 > maxnum:
    maxnum = num04
print("max number is "+str(maxnum))
