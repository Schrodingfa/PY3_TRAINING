# Author:jxy
# 定义函数 整数相加的参数

def count_int(*args):
    r = 0
    for i in args:
        r += i
    return r

print(count_int(12,563,2346,3,56,7))
