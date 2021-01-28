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
