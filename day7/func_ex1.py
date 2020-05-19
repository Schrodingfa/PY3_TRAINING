# Author:jxy
# 统计一个方法的调用次数

g01 = 0
def fun01():
    global g01
    g01 += 1

fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
print(g01)