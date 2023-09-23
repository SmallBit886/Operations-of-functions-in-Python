#函数的参数定义
''''''
def fun(a,b=10):    #b为默认值参数
    print(a,b)

#函数的调用
fun(100)    #100 10
fun(20,30)  #20 30

print() #def print(self, *args, sep=' ', end='\n', file=None)://end='\n'  默认值‘\n’
print('hello')
print('world')
'''
hello
world
'''

print('hello',end='\t')
print('world')
'''hello	world'''

print('hello',end='\r')
print('world')
'''world'''

print('hello',end='\b')
print('world')
'''hellworld'''