# 在控制台中录入一个整数，判断是否为素数
# 只能被1和本身整除的数字
# 如 9 判断9能否被2--8之间的数字整除，如果能则不是素数；如果都不能说明是素数
# 提示 循环出2--该数字-1之间的整数，再判断能否被整除

target = int(input("please input a number:"))
flag = True
if target < 2:
    print(False)
else:
    for i in range(2,target-1):
        if target % i == 0:
            flag = False
            break
    print(flag)

# target = int(input("please input a number:"))
# if target < 2:
#     print(False)
# else:
#     for i in range(2,target-1):
#         if target % i == 0:
#             print(False)
#             break
#     else:
#         print(True)
