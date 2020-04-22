# Author:jxy
# [1,4,7,4,8,0,6]
# 对列表进行排序
# 核心：发现更大的或更小的进行交换

list1 = [1,4,7,4,8,0,6]


for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)
