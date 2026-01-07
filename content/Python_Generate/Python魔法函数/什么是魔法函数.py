#! -*- encoding=utf-8 -*-
# 演示Python魔法函数 - 通过实现__getitem__使对象支持索引和迭代

class Company(object):
    """公司类 - 演示魔法函数的使用"""
    
    def __init__(self, employee_list):
        """初始化公司对象
        
        Args:
            employee_list: 员工列表
        """
        self.employee = employee_list
    
    def __getitem__(self, item):
        """实现索引访问和迭代协议
        
        Args:
            item: 索引位置
            
        Returns:
            返回对应位置的员工
            
        Note:
            通过实现__getitem__，使得对象可以像列表一样被索引访问
            同时也支持for循环迭代
        """
        return self.employee[item]

# 创建公司实例，传入员工列表
company = Company(["tom", "bob", "jane"])

# 方式1：直接访问employee属性进行迭代
employee = company.employee
for em in employee:
    print(em)

'''
输出：
tom
bob
jane
'''
'''
'''
以双下划线开头，以双下划线结尾的方法,一定使用python提供给我们的魔法函数
魔法函数为了增强自建类的特性

魔法函数说明：
- __getitem__: 实现索引访问，obj[key]
- __setitem__: 实现索引赋值，obj[key] = value
- __delitem__: 实现索引删除，del obj[key]
- __len__: 实现len()函数，len(obj)
- __iter__: 实现迭代器协议，返回迭代器对象
'''
# 方式2：直接迭代company对象（利用__getitem__魔法函数）
for em in company:
    print(em)
'''
输出：
tom
bob
jane
说明会自动去找构建时list里的值，for循环会自动找迭代器，而__iter__才会
生成迭代器，pyhton自身的优化就是在for拿不到迭代器的时候，会找这个__getitem__，
会一次一次的把数据全部取完。
'''
