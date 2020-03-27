# 在控制台中输入一个整数，根据整数打印一个正方形
# 4
# ****
# *  *
# *  *
# ****

num = int(input("please input a number:"))
print("*" * num)
for i in range(num - 2):
    print("*" + " " * (num - 2) + "*")
print("*" * num)
