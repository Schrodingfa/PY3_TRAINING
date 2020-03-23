# 在控制台中分别获取两个整数，一个作为开始值，一个作为结束值
# 请输出中间的数字

first = int(input("please input the first number:"))
last = int(input("please input the last number:"))

while first < last - 1:
    first += 1
    print(first)

