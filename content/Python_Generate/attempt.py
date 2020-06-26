#! -*- encoding=utf-8 -*-

def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 空数组
    if not nums:
        return -1

    sum_nums = sum(nums)
    left = 0  # 左起求的和
    # 遍历比较
    for i in range(len(nums)):
        if left * 2 == sum_nums - nums[i]:
            return i
        left += nums[i]
    return -1


# # 值类型互不影响，开辟了新的内存空间
# a = 1
# b = a
# print(id(a), id(b))
# a = 2
# print(b)
# print(id(a), id(b))

# print("*" * 80)

# # 引用类型影响，他们指向同一个对象
# c = {"age":2}
# d = c
# print(id(c), id(d))
# d["age"] = 3
# print(c.get("age"))
# print(id(c), id(d))

# print("*" * 80)
# # 值类型互不影响，开辟了新的内存空间
# e = None
# f = e
# print(id(e), id(f))
# f = "123"
# print(e)
# print(id(e), id(f))

# print("*" * 80)
# # 值类型互不影响，开辟了新的内存空间
# g = True
# h = g
# print(id(g), id(h))
# h = False
# print(g)
# print(id(g), id(h))

# d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
# d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
# d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
# d4 = dict(name='jason', age=20, gender='male') 
# print(d1 == d2 == d3 ==d4)
# print(id(d1), id(d2), id(d3), id(d4))


# s1 = 'hello'
# s2 = "hello"
# s3 = """hello"""
# print(id(s1),id(s2), id(s3))


# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l2
# print(id(l1), id(l2))

# def func(d):
#     d['a'] = 10
#     d['b'] = 20
# d = {'a': 1, 'b': 2}
# func(d)
# print(d)

# import time
# import functools
# import dis
# def log_execution_time(func): 
#     @functools.wraps(func) 
#     def wrapper(*args, **kwargs): 
#         start = time.perf_counter() 
#         res =func(*args, **kwargs) 
#         end = time.perf_counter() 
#         print('{} took {} ms'.format(func.__name__, (end - start) * 1000)) 
#         return res
#     return wrapper

# @log_execution_time
# def calculate_similarity(message):
#     print(message)
# print(dis.dis(calculate_similarity))
# calculate_similarity("123")

# # 以下一样

# def log_execution_time2(func): 
#     @functools.wraps(func) 
#     def wrapper(*args, **kwargs): 
#         start = time.perf_counter() 
#         func(*args, **kwargs) 
#         end = time.perf_counter() 
#         print('{} took {} ms'.format(func.__name__, (end - start) * 1000)) 
#     return wrapper

# @log_execution_time
# def calculate_similarity2(message):
#     print(message)
# print(dis.dis(calculate_similarity2))
# calculate_similarity2("123")

# import dis
# def index_generator(L, target): 
#     for i, num in enumerate(L): 
#         if num == target: 
#             yield i

# print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
# print(dis.dis(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))


# import dis
# def gen_func():
#     yield 1
#     yield 2
#     yield 3
#     return "fzk"

# if __name__ == "__main__":
#     gen = gen_func()
#     a = list(gen)
#     print(a,gen)

# import dis
# def gen_func():
#     html = yield "lalalalalala"
#     print(html)
#     yield 2
#     yield 3
#     return "fzk"

# if __name__ == "__main__":
#     gen = gen_func()
#     print(gen.send(None))
#     html = "fzk"
#     print(gen.send(html))
#     print(next(gen))


# def gen_func():
#     try:
#         yield "fzkfzkfzfk"
#     except Exception as e:
#         pass
#     yield 2
#     yield 3
#     return "123230482309481343243"

# if __name__ == "__main__":
#     gen = gen_func()
#     print(next(gen))
#     print(gen.throw(Exception, "download error"))   # 把2yield出来
#     print(next(gen))

a = {10: 2, 4: 5, 6: 7}
b = sorted(a.items())
print(b)
args = ("!", "werqwer")
c = ', '.join(repr(arg) for arg in args)
print(c)


class Zombin:
    def __init__(self):
        self.__zombin_blood = None
        self.__zombinBlood = None

    def run(self):
        pass

    def pace(self):
        pass

    def runtype(self):
        pass


z = Zombin()


class Plant:
    pass


from itertools import islice

batch_size = 10
t = [i for i in range(100)]
objs = (i for i in range(100))
print(objs)
while True:
    batch = list(islice(objs, batch_size))
    if not batch:
        break
    print(batch)

def testttt(args):
    print(args)
    print(*args)
    for a in args:
        print(a)

a = ["a", "b", "c", "www"]
testttt(a)

print(len({1:2}))
print({} is None)


print(" ".join(["1", "2", "44"]))

import re

ttt = re.split(r'([A-Z][a-z]*)', "BowAndTax")
print(" ".join(ttt).strip())
