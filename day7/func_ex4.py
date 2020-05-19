# Author:jxy
def fun06(*args, **kwargs):
    print(args)
    print(kwargs)


fun06(2, 45, 'sdf', 134, a=3, b=4, c='like')

def fun07(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

fun07(1,2,3,4,5,6,c=7,d=8,e='e',f='z',g='end')