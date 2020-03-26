# Author:jxy
# 显示120的倒计时
# 02:00 01:59 ...... 00:00

for i in range(120,-1,-1):
    m = i // 60
    s = i % 60
    print("%02d:%02d"%(m,s))


