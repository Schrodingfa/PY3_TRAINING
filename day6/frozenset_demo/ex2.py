# 经理：[曹操，刘备，孙权] 技术员：[曹操，刘备，张飞，关羽]
# 1.既是经理又是技术员的有谁
# 2.是经理但不是技术员的有谁
# 3.是技术员但不是经理的有谁
# 4.张飞是经理吗？
# 5.只有一个职务的有谁？
# 6.经理和技术员总共有多少人？
# 要求用集合完成

leader = ["曹操", "刘备", "孙权"]
employee = ["曹操", "刘备", "张飞", "关羽"]

l = frozenset(leader)
e = frozenset(employee)
# 1
print("既是经理又是技术员的是：")
for i in l & e:
    print(i)
print("**************************")
# 2
print("是经理但不是技术员的是：")
for i in l - e:
    print(i)
print("**************************")
# 3
print("是技术员但不是经理的是：")
for i in e - l:
    print(i)
print("**************************")
# 4
item = frozenset("张飞")
if item < l:
    print("张飞是经理")
else:
    print("张飞不是经理")
print("**************************")
# 5
print("只有一个职务的有：")
for i in e ^ l:
    print(i)
print("**************************")
# 6
count = len(l | e)
print("经理和技术员总共有" + str(count) + "人")
