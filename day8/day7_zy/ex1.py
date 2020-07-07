# Author:jxy
# 自定义列表的排序函数
# 提示 需要返回值吗？
# 不需要返回值 画内存图可以看出

def sort(list01):
    # 传入的是可变类型
    # 修改的是传入对象
    for i in range(len(list01) - 1):
        for j in range(i + 1, len(list01)):
            if list01[i] > list01[j]:
                list01[i], list01[j] = list01[j], list01[i]


l01 = [1, 4, 7, 4, 8, 0, 6]

sort(l01)
print(l01)
