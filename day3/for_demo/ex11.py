# 随机加法考试
# 随机产生两个数字 8 10
# 在控制台中获取两个数字的相加结果
# 如果输入正确成绩累加10分
# 如果输入错误成绩扣除5分
# 总共5题

import random
score = 0
for i in range(5):
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    res = int(input(str(num1)+"+"+str(num2)+"="))
    if res == num1 + num2:
        score += 10
    else:
        score -= 5
print("your score is "+str(score))
