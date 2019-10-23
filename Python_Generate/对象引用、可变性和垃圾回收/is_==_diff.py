#! -*- encoding=utf-8 -*-

c = [1,2,3]
d = c
print(id(c),id(d))
print(c is d)

a = [1,2,3,4]
b = [1,2,3,4]
print(id(a), id(b))
print(a is b)       # False
'''
所以只要有赋值符号=时，就回到上个文件的讲解
他会新创建一个对象[1,2,3,4]，然后再贴便利贴b
'''
# python内部有个机制，intern，对于小整数和小段字符串，都是会只生成一个全局变量，
# 再次遇见同一个对象他就不会再生成新的了。比如如下例子
e = 1
f = 1
print(id(e), id(f))
print(e is f)

g = "abc"
h = "abc"
print(id(g), id(h))
print(g is h)

# #########################################################################
print(a == b)
# 输出为：True
'''
== 是调用__eq__这个魔法函数
他是去判断值是否相等，只是他们不是一个对象而已
'''

class People:
    pass

person = People()
# 最常用用法：if isinstance(person, People)
if type(person) is People:
    print("yesy!yeah!")
'''
这个type的用法可行的原因：类本身就是一个对象，并且全局就这一个
所以用is判断的时候，他们俩的id是一样的，所以可行
'''
print(id(type(person)), id(People))
