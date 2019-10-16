class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a dog")

class Duck(object):
    def say(self):
        print("i am duck")

animal = Cat
animal().say()

# Java做法
'''
class Animal():
    def say(self):
        print("i am a animal")

class Cats(Animal):
    def say(self):
        print("i am a cat")
'''
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

'''
他们都有say，所以可以理解他们三个类都是属于一种类型
'''
print("##########################################################")

a = ["abc1", "abc2"]
b = ["abc2", "abc"]
name_tuple = ("abc3", "abc4")
name_set = set()
name_set.add("abc5")
name_set.add("abc6")
'''
a.extend(b)
print(a)
输出：['abc1', 'abc2', 'abc2', 'abc']
'''
'''
a.extend(name_tuple)
print(a)
输出：['abc1', 'abc2', 'abc3', 'abc4']
'''
'''
a.extend(name_set)
print(a)
输出：['abc1', 'abc2', 'abc5', 'abc6']
'''

'''
extend接收一个可迭代的对象，所以不仅仅局限于说list啊set啊这些常用的，
我们自己写的类实现了可迭代的方法，也可以传给这个函数
'''
'''
鸭子类型与魔法函数结合的理解
'''