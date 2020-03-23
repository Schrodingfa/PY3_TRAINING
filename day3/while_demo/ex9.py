# Author:jxy
# 猜数字 1.0
# 规则：系统生成 1 -- 100 之间的随机数
#      让用户一直猜，直到猜对为止
#      提示：大了 小了 猜对了
# 猜数字 2.0
# 最多只能猜10次
import random

# 1.0
# goal = random.randint(1,100) #产生随机数
# while True:
#     num = int(input("please input a number:"))
#     flag += 1
#     if num > goal:
#         print("too bigger")
#     elif num < goal:
#         print("too small")
#     else:
#         print("bingo!")
#         break

# 2.0
goal = random.randint(1,100) #产生随机数
flag = 0

while flag < 10: # 0 -- 9
    num = int(input("please input a number:"))
    flag += 1
    if num > goal:
        print("too bigger")
    elif num < goal:
        print("too small")
    else:
        print("bingo!")
        break
    # if flag == 10:
    #     print("you have try too many times.")
else:
    # 只有while条件不符合才会执行else语句
    # 从循环体内部break不会执行
    print("you have try too many times.")