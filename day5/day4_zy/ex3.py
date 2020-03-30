# 一注彩票7个球
# 其中前六个是红球 1 -- 33 之间的整数，且不重复
# 最后一个是蓝球 1 -- 16 之间的整数
# 1.在控制台中购买彩票 依次输入号码（保证以上条件）
# 2.随机产生一注彩票
# 3.对比两注彩票

import random

# user_number = []
# win_number = []
# flag = 1
#
# # user choice number
# while True:
#     num = int(input("please in the %dth number:" % (flag)))
#     if flag < 7:
#         if num < 1 or num > 33:
#             print("the number you choice is out of range")
#             continue
#         else:
#             if num in user_number:
#                 print("the number you choice is exist")
#                 continue
#             else:
#                 user_number.append(num)
#                 flag += 1
#     elif flag == 7:
#         if num < 1 or num > 16:
#             print("the number you choice is out of range")
#             continue
#         else:
#             user_number.append(num)
#             flag = 1
#             break
# print(user_number)
#
# # create winning number
# while True:
#     if flag < 7:
#         num = random.randint(1,33)
#         if num not in win_number:
#             win_number.append(num)
#             flag += 1
#         else:
#             continue
#     if flag == 7:
#         num = random.randint(1, 16)
#         win_number.append(num)
#         break
# print(win_number)


# 人选
ticket = []
# 前6个红球
while len(ticket) < 6:
    num = int(input("please in the %dth number:" % (len(ticket)+1)))
    if num < 1 or num > 33:
        print("the number you choice is out of range")
    elif num in ticket:
        print("the number you choice is exist")
    else:
        ticket.append(num)
# 蓝球
while True:
    num = int(input("please in the blue ball number:" ))
    if 1 <= num <= 16:
        ticket.append(num)
        break
    else:
        print("the number you choice is out of range")

# print(ticket)  # 只是将列表转换为字符串再显示、
# 获取每一个元素
for item in ticket:
    print(item)

# 机选
win_ticket = []
while len(win_ticket) < 6:
    num = random.randint(1, 33)
    if num not in win_ticket:
        win_ticket.append(num)
# # 排序
# win_ticket.sort()
win_ticket.append(random.randint(1,16))
# 对列表中指定范围的元素进行排序 利用切片
tmp = win_ticket[:6]
tmp.sort()
win_ticket[:6] = tmp
for item in win_ticket:
    print(item)