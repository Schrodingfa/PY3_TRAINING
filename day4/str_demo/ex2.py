# Author:jxy
# 再控制台中循环输入编码值，显示字符，直到输入负数是退出

while True:
    num = int(input("please input a number:"))
    if num < 0:
        break
    print(chr(num))