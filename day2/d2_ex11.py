# Author:jxy
# 如果钱不够，提示还需支付多少钱
# 如果钱够，提示需找零多少
# 尝试：若总金额达到100元打8折

unit_price = float(input("please input unit price:"))
count = int(input("pleast input number:"))
total_price = unit_price * count
money = float(input("please input money:"))
if total_price >= 100:
    total_price *= 0.8
if total_price <= money:
    print("change is " + str(money - total_price))
else:
    print("must pay " + str(total_price - money))

# 调试：让程序在指定的行中断，然后逐句执行，审查程序运行过程以及变量的取值
# 1.在可能出错的行加断点
# 2.开始调试
# 3.命中断点后（断点行是蓝色的），逐语句执行F7
# ......（判断执行过程，以及变量取值）......
# 4.停止调试Ctrl+F2
