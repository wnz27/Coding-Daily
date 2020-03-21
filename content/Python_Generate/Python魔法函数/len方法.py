#! -*- encoding=utf-8 -*-

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __getitem__(self, item):
        return self.employee[item]
    
    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])
len(company)

'''
在python尽量使用原生的内置方法，这些方法往往走的是捷径，效率会很高。
比如len就是去找内部记录的一个长度，而不是遍历来取到长度。
魔法函数还是很有用的，类比一下for循环与__iter__以及__getitem__的关系来思考
'''