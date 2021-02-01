import time
#装饰器
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name):
    print("this is a function" + func_name)

f1("test func")

@decorator
def f2(func_name1, func_name2):
    print("this is func_name1" + func_name1)
    print("this is func_name2" + func_name2)

f2("farg1", "farg2")

@decorator
def f3(func_name1, func_name2, **kw):
    print("this is func_name1" + func_name1)
    print("this is func_name2" + func_name2)
    print(kw)

f3("farg1", "farg2", a=1, b=2, c = "123")