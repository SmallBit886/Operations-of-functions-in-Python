#函数的创建和调用
#函数的参数传递
''''''
'''函数的创建'''
def calc(a,b):      #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
    c=a+b
    return c
'''函数的调用'''
'''位置实参'''
result=calc(10,20)      #10，20称为实际参数的值，简称为实参，实参的位置是在函数的调用处
print(result)   #30

'''关键字实参'''
res=calc(b=10,a=20)
print(res)  #30