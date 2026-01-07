#! -*- encoding=utf-8 -*-
# 演示__len__魔法函数的使用

class Company(object):
    """公司类 - 演示__len__魔法函数"""
    
    def __init__(self, employee_list):
        """初始化公司对象
        
        Args:
            employee_list: 员工列表
        """
        self.employee = employee_list
    
    def __getitem__(self, item):
        """实现索引访问
        
        Args:
            item: 索引位置
            
        Returns:
            返回对应位置的员工
        """
        return self.employee[item]
    
    def __len__(self):
        """实现len()函数支持
        
        Returns:
            返回员工数量
            
        Note:
            实现__len__后，可以直接使用len(company)获取员工数量
            Python内置的len()函数会调用对象的__len__方法
        """
        return len(self.employee)

# 创建公司实例
company = Company(["tom", "bob", "jane"])

# 调用len()函数，会自动调用__len__方法
print(f"公司员工数量: {len(company)}")

'''
Python魔法函数性能优化说明：

1. 使用内置方法的优势：
   - Python的内置方法（如len）往往经过高度优化
   - 这些方法通常走的是"捷径"，直接访问对象的内部属性
   - 比如len()是直接获取对象内部记录的长度值，而不是遍历计数

2. 魔法函数的重要性：
   - 使自定义类能够使用Python的内置函数和操作符
   - 让自定义对象的行为更符合Python风格（Pythonic）
   - 提高代码的可读性和一致性

3. 类比思考：
   - for循环会先尝试调用__iter__获取迭代器
   - 如果没有__iter__，会尝试使用__getitem__通过索引迭代
   - 这种机制提供了灵活的迭代方式
'''