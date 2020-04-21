# Author:jxy
# 列表中是否有相同元素
# [1,4,7,4,8,0,6]
# 核心：所有元素间两两比较
# 思想：取出第一个元素，与后面进行比较，
#      取出第二个元素，与后面进行比较，
#      取出第三个元素，与后面进行比较，
#      …………

list1 = [1,4,7,4,8,0,6]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            print(list1[i])
