#! -*- encoding=utf-8 -*-
# 列表生成式（列表推导式）
# 1、提取出1-20之间的奇数
odd_list = []
for i in range(21):
    if i%2 == 1:
        odd_list.append(i)
print(odd_list)
# 列表推导式
a = [x for x in range(21) if x%2 ==1]
print(a)

# 2、逻辑复杂的情况
def handle_item(item):
    return item*item
print([handle_item(x) for x in range(21) if x%2 ==1])
'''
列表生成式即列表推导式性能高宇列表操作
'''

# 生成器表达式
lalala = (x for x in range(21) if x%2 ==1)
print(type(lalala))
print(lalala)
# 生成器可以直接转换为list, 直接作用在生成器上
la_list = list(lalala)
print(la_list)
# 生成器的对象我们可以通过for循环的方式打印出来，也是
lalala1 = (x for x in range(21) if x%2 ==1)
for item in lalala1:
    print(item)

# 字典推导式
my_dict = {"fzk": 154, "fzk2":123, "fzk3": 4666}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)
my_set1 = {key for key,value in reversed_dict.items()}
print(my_set1)

# 集合推导式
my_set = {key for key,value in my_dict.items()}
print(type(my_set))
print(my_set)
# 有简单方法,只是灵活性没有上面高
my_set3 = set(my_dict.keys())



