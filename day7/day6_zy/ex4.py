# Author:jxy
# 定义函数，判断字符串中存在的中文字符数量
# 中文编码范围：0x4E00 -- 0x9FA5
# 相关函数 ord(字符)

def count_of_cnstr(str):
    count = 0
    for i in str:
        if 0x4E00 <= ord(i) <= 0x9FA5:
            count += 1
    return count

str = "待统计string,lalala"
print(count_of_cnstr(str))