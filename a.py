###
print("hello python")
print("hello world")

from functools import reduce

list_x = [1,2,3,4,5,6,7,8]

#连续计算，连续调用lambda
r = reduce(lambda x,y:x+y, list_x)
print(r)

list_y = [1,0,1,0,0,1]
#过滤器
r1 = filter(lambda x:True if x == 1 else False, list_y)
print(list(r1))


#命令式编程


#装饰器
import time
def f1():
    print('This is a function')

#unix 时间戳
#f1()

def f2():
    print("this is a function2")

#对修改是封闭的，对扩展是开放的
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
###

#装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

def f1():
    print("this is a function")



f = decorator(f1)
f()