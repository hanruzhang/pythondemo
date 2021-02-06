#列表推导式
#集合推导式
#map filter
#set 也可以被推导
#dict

a = [1,2,3,4,5,6,7,8]
b = [i*i for i in a]
print(b)

c = {i**2 for i in a if i >= 5}
print(c)