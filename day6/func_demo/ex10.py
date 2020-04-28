# Author:jxy
# ex3升级版

def print_star(len,wid,cha):
    """
    打印一个矩形图形
    :param len: 矩形的行数
    :param wid: 矩形的宽度
    :param cha: 组成矩形的图形
    :return: 无返回值
    """
    for i in range(len):
        for j in range(wid):
            print(cha, end="")  # 不换行
        print()  # 换行

length = int(input('please input the length:'))
width = int(input('please input the width:'))
char = input('please input the char:')

print_star(length,width,char)
