# Author:jxy
# 定义函数，返回指定范围内的素数
# # 如 1--100
# target = int(input("please input a number:"))
# flag = True
# if target < 2:
#     print(False)
# else:
#     for i in range(2,target-1):
#         if target % i == 0:
#             flag = False
#             break
#     print(flag)



# def get_prime(start, end):
#     res = []
#     for i in range(start, end + 1):
#         if i < 2:
#             pass
#         else:
#             for j in range(2, i - 1):
#                 if i % j == 0:
#                     break
#             else :
#                 res.append(i)
#     return res



def get_prime(start, end):
    """
    生成指定范围内的所有素数
    :param start: 开始数字 int
    :param end: 结束数字 int
    :return: 范围内的所有素数 list
    """
    res = []
    for i in range(start, end + 1):
        if is_prime(i):
            res.append(i)
    return res


def is_prime(i):
    """
    判断一个整数是否为素数
    :param i: 目标数字 int
    :return: 返回是否为素数 bool
    """
    # 小于2 不是素数
    if i < 2:
        return False
    # 能否被中间数字整除
    for j in range(2, i - 1):
        if i % j == 0:
            return False
    else:
         return True


r = get_prime(1, 100)
print(r)
