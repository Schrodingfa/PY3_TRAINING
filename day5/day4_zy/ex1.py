# 在控制台中循环录入字符串，输入q时退出
# 将录入的字符串合成，显示一个新的字符串

str_list = []
while True:
    str = input("please input a string:")
    if str == "q":
        break
    else:
        str_list.append(str)
longstr = "".join(str_list)
print(longstr)
