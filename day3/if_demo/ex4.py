# 在控制台获取一个整数，判断是奇数还是偶数，要求使用真值表达式

num = int(input("please input a number:"))

# if num % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")


if num % 2: # bool(num % 2)
    print("奇数")
else:
    print("偶数")
