# Author:jxy
# 英文单词反转
# how are you --> you are how

str01 = "how are you"
str_s1 = str01.split()
# print(str_s1)
# str_s1.reverse()
str_s1 = str_s1[::-1]
# print(str_s1)
str02 = " ".join(str_s1)
print(str02)