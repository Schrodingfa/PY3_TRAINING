# Author:jxy
# 参照下列代码，定义获取最小值的方法
# min = list01[0]
# for i in range(1,len(list01)):
#     if min > list01[i]:
#         min = list01[i]
# print(min)

def min_of_list(list01):
    min = list01[0]
    for i in range(1,len(list01)):
        if min > list01[i]:
            min = list01[i]
    return min

a = [32,45,1,546,0,3452,6]
print(min_of_list(a))