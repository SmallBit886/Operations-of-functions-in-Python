#函数的参数的定义
''''''
'''使用*定义个数可变的位置形参'''
def fun(*a): #无法事先确定传递的位置实参的多少，使用可变的位置参数
    print(a)    #结果为一个元组
    print(a[0]) #结果为10
#结果为一个元组
fun(10) #(10,)
fun(10,30)  #(10, 30)
fun(10,30,40)   #(10, 30, 40)
#def print(self, *args, sep=' ', end='\n', file=None):

'''使用**定义个数可变的关键字形参'''
def fun1(**b): #无法事先确定传递的关键字实参的多少，使用可变的关键字参数
    print(b)
#结果为一个字典
fun1(a=10)  #{'a': 10}
fun1(a=10,b=20) #{'a': 10, 'b': 20}
fun1(a=10,b=20,c=30)    #{'a': 10, 'b': 20, 'c': 30}
'''可变的位置参数只能有一个'''
'''
def fun2(*a,*b):
    pass
'''
'''def fun2(*a,*b):
                ^
SyntaxError: invalid syntax
'''
'''可变的关键字参数只能有一个'''
'''
def fun2(**a,**b):
    pass
'''
'''
    def fun2(**a,**b):
                 ^
SyntaxError: invalid syntax
'''
'''在一个函数定义过程中，两种形参都有的话，要求，个数可变的位置形参，放在个数可变的关键字形参之前'''
'''
def fun2(**a,*b):
    pass
'''
'''
    def fun2(**a,*b):
                 ^
SyntaxError: invalid syntax
'''
def fun2(*a,**b):
    pass
