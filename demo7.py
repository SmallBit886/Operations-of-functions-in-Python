#变量的作用域
def fun(a,b):
    c=a+b   #c 为局部变量，因为c是在函数内进行定义的变量，a,b，为函数的形参，作用范围也在函数内部，相当于局部变量
    print(c)
'''    
print(a)
print(c)
超出了作用域；错误
'''

name='马老师'  #name的作用范围为函数内部和外部都可以使用  --》全局变量
print(name)
def fun1():
    print(name)
#调用函数
fun1()

def fun2():
    global age  #函数内部定义的变量，局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
    age=20
    print(age)

fun2()
print(age)
