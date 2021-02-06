#None 空
#空字符串 空的列表 0 False

class Test():
    def __len__(self):
        return True;
    def __bool__(self):
        return False

test = Test()
print(bool(None))
print(bool([]))
print(bool(test))
#打印结果为F
if test:
    print('S')
else:
    print('F')