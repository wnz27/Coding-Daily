#! -*- encoding=utf-8 -*-

from random import randint

import os
file_name = "123.txt"
root = os.getcwd()
file_path_name = os.path.join(root, file_name)

def load_list_data(total_nums, target_nums):
    """
    从文件中读取数据，以list的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = []
    target_data = []
    # file_name = "fbobject_idnew.txt"
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data.append(line)
            else:
                break

    for x in range(target_nums):
        random_index = randint(0, total_nums)
        if all_data[random_index] not in target_data:
            target_data.append(all_data[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data

def load_dict_data(total_nums, target_nums):
    """
    从文件中读取数据，以dict的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = {}
    target_data = []
    # file_name = "fbobject_idnew.txt"
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data[line] = 0
            else:
                break
    all_data_list = list(all_data)
    for x in range(target_nums):
        random_index = randint(0, total_nums-1)
        if all_data_list[random_index] not in target_data:
            target_data.append(all_data_list[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data

  

def find_test(all_data, target_data):
    #测试运行时间
    test_times = 100
    total_times = 0
    import time
    for i in range(test_times):
        find = 0
        start_time = time.time()
        for data in target_data:
            if data in all_data:
                find += 1
        last_time = time.time() - start_time
        total_times += last_time
    return total_times/test_times


if __name__ == "__main__":
    all_data, target_data = load_list_data(10000, 1000)
    # all_data, target_data = load_list_data(100000, 1000)
    # all_data, target_data = load_list_data(1000000, 1000)

    # all_data, target_data = load_dict_data(10000, 1000)
    # all_data, target_data = load_dict_data(100000, 1000)
    # all_data, target_data = load_dict_data(1000000, 1000)
    # all_data, target_data = load_dict_data(2000000, 1000)
    last_time = find_test(all_data, target_data)

    #dict查找的性能远远大于list
    #在list中随着list数据的增大 查找时间会增大
    #在dict中查找元素不会随着dict的增大而增大
    print(last_time)

#1.  dict的key或者set的值 都必须是可以hash的
#不可变对象 都是可hash的， str， fronzenset， tuple，自己实现的类 __hash__
#2. dict的内存花销大，但是查询速度快， 自定义的对象 或者python内部的对象都是用dict包装的
# 3. dict的存储顺序和元素添加顺序有关, 但是也可能改变，所以也是把dict当无顺序处理
# 4. 添加数据有可能改变已有数据的顺序，就是重新分配空间在复制的时候使用映射算法时可能就会改变顺序

# OrderdDict，有顺序的dict

'''
pyhton 内部还有一些实现是这样的
因为这些可哈希的要计算位置，比如拿dict举例
如果系统给这个dict分配的空间剩三分之一了，
那么就会重新去开辟一个更大的位置把里面元素拷贝
过去，因为如果不这样做，再添加元素的时候哈希计算位置的时候
冲突的概率会变得很大，所以python底层这样实现
'''

# set和dict的原理和性能是差不多的，而且set占用空间比dict少，且可去重