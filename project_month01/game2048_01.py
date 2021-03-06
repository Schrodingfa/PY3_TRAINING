# Author:jxy
# 2048 核心算法

# 练习1：定义函数，将0元素移动到末尾
# 2 0 2 0 --> 2 2 0 0
# 0 2 0 2 --> 2 2 0 0

# 思路一
# def zero_to_end(list01):
# 如果元素为零则与后面一个元素交换
#     for i in range(len(list01) - 1):
#         for j in range(i + 1, len(list01)):
#             if list01[i] == 0 and list01[j] != 0:
#                 list01[i], list01[j] = list01[j], list01[i]

# 思路二
# def zero_to_end(list_target):
#     # 1.将传入的列表中的非零元素拷贝到新列表中
#     # 2.根据零元素的数量，在新列表中补零
#     # new_list = []
#     # for item in list_target:
#     #     if item != 0 :
#     #         new_list.append(item)
#     new_list = [item for item in list_target if item != 0]
#     new_list += [0] * list_target.count(0)
#     # 3.将新列表中元素赋值给传入的列表
#     list_target[:] = new_list[:]

# 思路三
def zero_to_end(list_target):
    # 从后往前判断，如果是零元素，则删除，再在末尾追加零元
    # [2,0,2,0] --> [2,0,2] --> [2,0,2,0]
    # [2,2,0] --> [2,2,0,0]
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


# 练习2：定义合并函数
# 2 2 0 0 --> 4 0 0 0
# 2 0 2 0 --> 4 0 0 0
# 2 0 0 2 --> 4 0 0 0
# 2 2 2 0 --> 4 2 0 0

# def merge_num(list_target):
#     zero_to_end(list_target)
#     if list_target[0] == list_target[1]:
#         list_target[0] += list_target[1]
#         list_target.pop(1)
#         list_target.append(0)

def merge_num(list_target):
    for i in range(len(list_target) - 1):
        zero_to_end(list_target)
        if list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0


# l01=[2,0,4,2]
# merge_num(l01)
# print(l01)

# 练习3：将二维列表，以表格的形式显示在控制台中
list01 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]

def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print('%4d' %map[i][j],end=' ')
        print()

# print_map(list01)

# 练习4：定义向左移动函数
'''
[2, 0, 0, 2]    [4, 0, 0, 0]
[2, 2, 0, 0]    [4, 0, 0, 0]
[2, 0, 4, 4]    [2, 8, 0, 0]
[4, 0, 0, 2]    [4, 2, 0, 0]
'''

def move_left(map):
    for i in range(len(map)):
        # 从左往右获取行
        merge_num(map[i])

def move_right(map):
    for i in range(len(map)):
        # 从右往左获取行
        list_merge = map[i][::-1]
        merge_num(list_merge)
        map[i][::-1] = list_merge


# move_left(list01)
# # move_right(list01)
# print_map(list01)

# 作业1：定义向上移动函数
# 从上往下获取列
# 交给合并方法
# 还给原列

def move_up(map):
    for i in range(len(map)):
        list_merge = []
        for j in range(len(map)):
            list_merge.append(map[j][i])
        merge_num(list_merge)
        for j in range(len(map)):
            map[j][i]=list_merge[j]

# move_up(list01)
# print_map(list01)

# 作业2：定义向下移动函数
# 从下往上获取列
# 交给合并方法
# 还给原列

def move_down(map):
    for i in range(len(map)):
        list_merge = []
        for j in range(len(map)):
            list_merge.append(map[j][i])
        list_merge.reverse()
        merge_num(list_merge)
        list_merge.reverse()
        for j in range(len(map)):
            map[j][i]=list_merge[j]

move_down(list01)
print_map(list01)