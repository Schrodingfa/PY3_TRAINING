# Author:jxy
# 参照下列代码，定义判断是否是奇数的方法。
# number = int(input("请输入一个整数："))
# if number % 2 == 1:
#     print("奇数")
# else:
#     print("偶数")

def check_odd(number):
    # if number % 2 == 1:
    #     return True
    # return False
    # return True if number % 2 == 1 else False
    return number % 2 == 1


# number = int(input("请输入一个整数："))
print(check_odd(7))
