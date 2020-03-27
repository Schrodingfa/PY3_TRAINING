# 在控制台中录入学生姓名
# 要求：姓名不能重复
#      如果录入esc，则停止录入，打印每个学生姓名

# name_list = []
# while True:
#     name = input("please input a student name:")
#     if name == "esc":
#         break
#     elif name in name_list:
#         print("this student is exist, please input anothe one.")
#         continue
#     else:
#         name_list.append(name)
# for i in name_list:
#     print(i)


name_list = []
while True:
    name = input("please input %dth student's name:"%(len(name_list)+1))
    if name == "esc":
        break
    elif name not in name_list:
        name_list.append(name)

for i in name_list:
    print(i)