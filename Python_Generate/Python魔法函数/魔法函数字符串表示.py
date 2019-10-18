#! -*- encoding=utf-8 -*-

'''
字符串表示：
__repr__
__str__
'''
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __str__(self):
        return ",".join(self.employee)
    
    def __repe__(self):
        return ",".join(self.employee)

company = Company(["tom", "bob", "jane"])
print(company)
company # 什么都不会输出，但是在解释器环境下写这个变量会自动调用__repr__
# 输出：<__main__.Company object at 0x1006de518>
'''
定义__str__后再打印输出：
tom,bob,jane
'''

'''
__repr__ 这是开发模式下用的
__str__  这是对对象进行字符串格式化的时候调用的
'''