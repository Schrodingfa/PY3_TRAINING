# 在控制台录入学生成绩
# 请输入学生总数
# 请输入第一个学生的成绩：
# ……
# 计算总分，最高分，最低分

score_list = []
count = int(input("please input the number of student:"))
for i in range(count):
    score = int(input("please the %dth student's score:" % (i + 1)))
    score_list.append(score)
print(score_list)
print("the sum of score is %d." % sum(score_list))
print("the max of score is %d." % max(score_list))
print("the min of score is %d." % min(score_list))
