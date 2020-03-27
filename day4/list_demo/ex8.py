# 找出列表中的最大值，不可以使用max函数

list1 = [34, 5, 6, 78, 9, 0, 5, 8, 88, 4]
# maxnum = 0
# for i in list1:
#     if i > maxnum:
#         maxnum = i
#
# print(maxnum)

# 假设第一个元素就是最大值
max = list1[0]
# 依次与后面（从第二个开始）元素进行比较
for i in range(1,len(list1)):
    # 发现更大值则替换假设
    if max < list1[i]:
        max = list1[i]
#最后假设的就是最大值
print(max)

# 找出最小的元素
min = list1[0]
for i in list1[1:]: # 使用切片会产生一个新的列表，如果元素过多则浪费资源，不建议
    if min > i:
        min = i
print(max)
