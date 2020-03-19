# Author:jxy

a = input("变量a:")
b = input("变量b:")

# 利用临时变量交换
# c = a
# a = b
# b = c
a, b = b, a  # 直接交换

print("变量a为", a, "变量b为", b)
