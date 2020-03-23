# 累加1 -- 100 之间 能被3整除的整数和

# count = 0
# for i in range(100):
#     if not ( i + 1 ) % 3 :
#         count += ( i + 1 )
#     else:
#         continue
# print(count)

# count = 0
# for i in range(1, 100):
#     # 如果满足条件则累加
#     if not i % 3 :
#         count += i
# print(count)

count = 0
for i in range(1, 100):
    # 如果不满足条件则跳过
    if i % 3 :
        continue
    count += i
print(count)