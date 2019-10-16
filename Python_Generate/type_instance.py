class A: 
    pass

class B(A):
    pass

b = B()
print(isinstance(b, B))     # True, b是不是B的实例
print(isinstance(b, A))     # True, b是不是A的实例

print(type(b))  # 输出<class '__main__.B'>

print(id(B))
print(type(b) is B)  # is是判断是不是同一个对象，就是判断id是否相同, 输出：True
print(type(b) == B)  # ==是判断值是否相等, 输出: True

print(type(b) is A)  # 输出：False。 type(b)已经指向B了，所以和A的地址不可能相同

'''
所以判断实例的类型时尽量用isinstance即可，用type可能出一些问题，误差。
'''