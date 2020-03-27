# 回文 eg 上海自来水来自海上
# 判断一个字符串是否是回文
# 提示 字符串翻转

str = input("please input a string:")
if str == str[::-1]:
    print("true")
else:
    print("false")

