#! -*- encoding=utf-8 -*-

# 模式[start:end:step]
'''
    其中，第一个数字start表示切片开始位置，默认为0；
    第二个数字end表示切片截止（但不包含）位置（默认为列表长度）；
    第三个数字step表示切片的步长（默认为1）。
    当start为0时可以省略，当end为列表长度时可以省略，
    当step为1时可以省略，并且省略步长时可以同时省略最后一个冒号。
    另外，当step为负整数时，表示反向切片，这时start应该比end的值要大才行。 
'''
aList = [3,5,6,7,9,11,13,15,17]

print(aList[::])    # 返回包含原列表中所有元素的新列表
print("*" * 80)
print(aList[::-1])  # 返回包含原列表中所有元素的逆序列表
print("*" * 80)
print(aList[::2])   # 隔一个取一个，获取偶数位置的元素
print("*" * 80)
print(aList[1::2])  # 隔一个取一个，获取奇数未知的元素
print("*" * 80)
print(aList[3:6])   # 指定切片开始和结束（不包含）的位置
print("*" * 80)
print(aList[0:100]) # 切片结束的位置大于列表长度时，从尾部截断
print("*" * 80)
print(aList[100:])  # 切片开始位置大于列表长度时，返回空列表
print("*" * 80)
print("############# 操作列表！！！！！牛逼啊啊啊##############")
print("*" * 80)
aList[len(aList):] = [9]    # 在列表结尾增加元素
print(aList)
print("*" * 80)
aList[:0] = [1,2]       # 在列表头部插入元素 等价于aList = [1,2] + aList
print(aList)
print("*" * 80)
aList[3:3] = [4]        # 在列表中间插入元素
print(aList)
print("*" * 80)
aList[:3] = [900,800,700]   # 替换列表元素，等号两边的列表长度相等
print(aList)
print("*" * 80)
aList[3:] = [2,5,7]     # 等号两边的列表长度也可以不相等
print(aList)
print("*" * 80)
aList[::2] = [1] * 3    # 隔一个修改一个,乘号后面的数指的要修改几个，因为左侧切片不连续。所以必须写对.[1] * 3  = [0,0,0]
print(aList)
print("*" * 80)
aList[::2] = ['a', 'b', 'c']    # 隔一个修改一个,因为左侧切片不连续，列表个数也必须对应写对
print(aList)
print("*" * 80)
# aList[::2] = ["a", "b"]
'''
上面这个就会报错：
Traceback (most recent call last):
  File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/Python自定义序列类/实现可切片对象.py", line 48, in <module>
    aList[::2] = ['a', 'b'] 
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
'''
aList[:3] = []      # 删除列表中前三个元素
print(aList)
print("*" * 80)
# del aList[:3]         # 切片元素梁旭删除
del aList[::2]          # 切片元素不连续删除，隔一个删一个，删偶数位置
print(aList)