#函数的返回值
''''''
print(bool(0))  #False
print(bool(3))  #Ture

def fun(num):
    odd=[]  #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

#函数的调用
lst=[10,29,34,23,44,53,55]
print(fun(lst)) #元组 ([29, 23, 53, 55], [10, 34, 44])

'''
函数的返回值
（1）如果函数没有返回值【函数执行完成之后，不需要给调用处提供数据】return可以省略不写
（2）函数的返回值，如果是1个，直接返回类型
（3）函数的返回值，如果是多个，返回的结果为元组
'''

def fun1():
    print('hello')
    #return
fun1()  #hello

def fun2():
    return 'hello'

res=fun2()
print(res)  #hello

def fun3():
    return 'hello','world'

print(fun3())   #('hello', 'world')
'''函数在定义时，是否需要返回值，视情况而定'''
