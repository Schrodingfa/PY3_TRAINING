# Author:jxy
# 温度换算器
# 输入华氏度，输出摄氏度
# 输入摄氏度，输出华氏度和开式度

choice = input("1 Fahrenheit degree\t2 Celsius degree\nwhice one would you input:")
degree = float(input("input the degree:"))
if choice == "1":
    c_degree = (degree - 32) / 1.8
    print("Celsius degree is " + str(c_degree))
elif choice == "2":
    f_degree = degree * 1.8 + 32
    k_degree = degree + 273.15
    print("Fahrenheit degree is " + str(f_degree))
    print("Kelvin degree is " + str(k_degree))
else:
    print("invalid parameter")
