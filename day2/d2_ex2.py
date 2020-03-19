# Author:jxy

hour = int(input("小时："))
minute = int(input("分钟："))
second = int(input("秒："))
account = hour * 3600 + minute * 60 + second

print("共"+str(account)+"秒。")
