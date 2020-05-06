# Author:jxy
# 定义函数，返回指定范围内的素数
# 如 1--100

def print_prime(start,end):
    res = []
    for i in range(start,end+1):
        flag = True
        if i == 2:
            res.append(i)
            continue
        else:
            for j in range(2,i):
                if i % j == 0:
                    flag = False
                    break
        if flag :
            res.append(i)
    return res

r = print_prime(2,13)
print(r)