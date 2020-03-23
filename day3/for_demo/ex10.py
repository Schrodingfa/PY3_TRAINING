# Author:jxy

for i in range(5):
    var01 = input("please input the first var:")
    var02 = input("please input the second var:")
    var01, var02 = var02, var01
    print("first var is "+var01+", second var is "+var02)