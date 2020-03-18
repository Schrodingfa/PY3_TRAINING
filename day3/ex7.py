# 一张纸的厚度是0.1mm
# 需要对折多少次可以超过珠穆朗玛峰的高度 8844.43

flag = 0
paper = 0.0001
m = 8844.43

while paper < m:
    paper *= 2
    flag += 1
print(flag)