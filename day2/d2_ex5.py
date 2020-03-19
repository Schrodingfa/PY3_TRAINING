# Author:jxy

number = int(input("please enter a number:"))
# number1 = number // 1000
# number2 = (number - number1 * 1000) // 100
# number3 = (number % 100 - (number % 10)) // 10
# number4 = number % 10

# number4 = number % 10
# number3 = number // 10 % 10
# number2 = number // 100 % 10
# number1 = number // 1000
# 也可使用累加
# print(number1 + number2 + number3 + number4)
# 也可使用累加
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000

print(result)
