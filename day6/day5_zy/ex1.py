# Author:jxy
# 在控制台中录入5个学生信息（姓名，年龄，性别）
# 用什么样的数据结构表达学生信息
# 数据结构：列表中嵌套字典
# [
#     {
#         "name":xx,
#         "age":xx,
#         "sex":xx
#     },
#     {
#         "name":xx,
#         "age":xx,
#         "sex":xx
#     }
#     ......
# ]
# 打印学生信息

list01 = []
dict01 = {}

for i in range(5):
    dict01["name"] = input("please input name:")
    dict01["age"] = input("please input age:")
    dict01["sex"] = input("please input sex:")
    list01.append(dict01)
print("\n")
for i in list01:
    for k, v in i.items():
        print("%s is %s." % (k, v))
    print("\n")
