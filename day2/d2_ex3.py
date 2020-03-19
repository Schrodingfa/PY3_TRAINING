# Author:jxy

unit1 = int(input("请输入两数："))
unit2_1 = unit1 // 16
unit2_2 = (unit1 % 16) * 10 // 16

print("共"+str(unit2_1)+"斤"+str(unit2_2)+"两")
