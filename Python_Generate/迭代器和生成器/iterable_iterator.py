#! -*- encoding=utf-8 -*-
from collections.abc import Iterator, Iterable

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __iter__(self):
        #return 1
        '''
        Traceback (most recent call last):
        File "/Users/fzk27/fzk27/Coding-Daily/Python_Generate/迭代器和生成器/iterable_iterator.py", line 15, in <module>
        my_itor = iter(company)
        TypeError: iter() returned non-iterator of type 'int'
        ''' 
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]

class MyIterator(Iterator):     # 继承了Iterator之后就不需要再写__iter__方法了因为Iterator已经实现了
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == "__main__":

    company = Company(["fzk", "fzk1", "fzk2"])
    my_itor = iter(company)
    while True:
        try:
            print(next(my_itor))
        except StopIteration as e:
            pass

    # for item in company:
    #     print(item)
