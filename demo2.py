#实参和形参的名字可以不一样
''''''
'''在函数的调用过程中，进行参数的传递
如果是不可变对象，在函数体内的修改不会影响实参的值 arg1的修改为100，不会影响n1的值
如果是可变对象，在函数体内的修改会影响到实参的值  arg2的修改，append（10），会影响到n2的值
'''
def fun(arg1,arg2):
    print(arg1)
    print(arg2)
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)

n1=11
n2=[22,33,44]
print('n1=',n1)
print('n2=',n2)
''' 
n1= 11
n2= [22, 33, 44]
'''

fun(n1,n2)
'''
11
[22, 33, 44]
arg1= 100
arg2= [22, 33, 44, 10]
'''

print('n1=',n1)
print('n2=',n2)
'''
n1= 11
n2= [22, 33, 44, 10]
'''
