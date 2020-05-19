# Author:jxy
# 定义函数 根据天/小时/分钟计算总秒数

def count_second(d=0, h=0, m=0):
    # d_to_s = d * 24 * 60 * 60
    # h_to_s = h * 60 * 60
    # m_to_s = m * 60
    # return d_to_s + h_to_s + m_to_s
    return d * 24 * 60 * 60 + h * 60 * 60 + m * 60


print(count_second(3, 2, 5))
print(count_second(d=1))
print(count_second(h=3))
