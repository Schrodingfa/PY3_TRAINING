"""
******
######
******
######
"""

for i in range(4):
    for j in range(6):
        if i % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()
