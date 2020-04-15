"""    空格    #
####         0123
 ###    0    012
  ##    01   01
   #    012  0
"""

for i in range(4):
    for k in range(i):
        print(" ", end="")
    for j in range(4-i):
        print("#",end="")
    print()