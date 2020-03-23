# 一个球从100m的高度落下，每次弹回原高度的一半
# 总共能弹起多少次(假定最小弹起高度是0.01m)
# 总共走了多少米

hight = 100
length = hight
flag = 0
# 弹起来的高度>=0.01
while hight / 2 >= 0.01:
    hight /= 2
    flag += 1
    length += hight * 2 # 累加上下距离
    print(str(flag)+"\t"+str(hight))

length = round(length,2) # 保留两位小数
print("the length is "+str(length)+", and flag is "+str(flag)+".")
