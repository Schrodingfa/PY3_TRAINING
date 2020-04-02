# Author:jxy
# ["张三丰","无忌","赵敏"]
# [101,102,103]
# 1.根据两个列表形成一个字典：key姓名，value房间号
# 2.将字典的键与值进行翻转

name = ["张三丰", "无忌", "赵敏"]
room = [101, 102, 103]

# d01 = {}
# for i in range(3):
#     d01[name[i]] = room[i]
d01 = {name[i]: room[i] for i in range(len(name))}
print(d01)

# d02 = {}
# for k,v in d01.items():
#     d02[v] = k
d02 = {v: k for k, v in d01.items()}
print(d02)
