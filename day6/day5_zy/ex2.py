# Author:jxy
# 猜拳
# 规则：系统随机出拳，在控制台中循环猜测
# 提示：1、将胜利的策略存入容器
#      （
#           （“石头”，“剪刀”），
#           （“剪刀”，“布”），
#           （“布”，“石头”）
#       ）
#       2、将用户猜的拳与系统出拳形成一个元组

import random

win = (("石头", "剪刀"), ("剪刀", "布"), ("布", "石头"))
# loss = (("剪刀","石头"),("布","剪刀"),("石头","布"))

while True:
    ranstr = random.choice(("石头", "剪刀", "布"))
    inpstr = input("please input you choice:")
    t = (inpstr, ranstr)
    if inpstr == "q":
        print("Quit")
        break
    elif inpstr == ranstr:
        print("It ends in a draw.")
    elif t in win:
        print("You are win.")
    else:
        print("You are loss.")
