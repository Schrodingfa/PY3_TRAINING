# Author:jxy
# ex5升级版

def pri_triangle(r,c):
    """
    打印三角形
    :param r: 三角形高度
    :param c: 组成三角形的字符
    :return: 无返回值
    """
    for i in range(r):
        for j in range(i+1):
            print(c,end="")
        print()

row = int(input("please input the triangle's row:"))
char = input('please input the char:')

pri_triangle(row,char)
