# Author:jxy
# ex7 升级版
# 定义一个检查列表中是否有相同元素的方法

def check_list(l):
    # flag = False #假设无相同元素
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                return True # 可以退出两层循环体
        #         flag = True
        #         break # 只能退出就近循环体
        # if flag:
        #     break
    return False

res = check_list([1,4,7,8,0,6])

print(res)
