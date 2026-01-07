#! -*- encoding=utf-8 -*-
# 演示字符串表示魔法函数：__str__ 和 __repr__

'''
字符串表示魔法函数说明：

1. __repr__：
   - 用于开发者阅读，提供对象的“官方”字符串表示
   - 在交互式解释器中直接输入对象名时调用
   - 应该返回一个能够重新创建该对象的字符串（理想情况）
   - 如果未定义，默认显示 <类名 object at 内存地址>

2. __str__：
   - 用于用户阅读，提供对象的“友好”字符串表示
   - 在使用print()函数或str()转换时调用
   - 应该返回一个易于阅读的字符串
   - 如果未定义__str__，会退而使用__repr__

3. 优先级：
   - print(obj) → 调用 __str__（如果存在）
   - obj 在解释器中 → 调用 __repr__
   - 如果只定义一个，建议定义 __repr__
'''

class Company(object):
    """公司类 - 演示字符串表示魔法函数"""
    
    def __init__(self, employee_list):
        """初始化公司对象
        
        Args:
            employee_list: 员工列表
        """
        self.employee = employee_list
    
    def __str__(self):
        """返回用户友好的字符串表示
        
        Returns:
            用逗号连接的员工姓名字符串
            
        Note:
            当使用print(company)时会调用此方法
        """
        return ",".join(self.employee)
    
    def __repr__(self):
        """返回开发者友好的字符串表示
        
        Returns:
            用逗号连接的员工姓名字符串
            
        Note:
            在解释器中直接输入company时会调用此方法
        """
        return ",".join(self.employee)

# 创建公司实例
company = Company(["tom", "bob", "jane"])

# 使用print()会调用__str__方法
print("print(company) 输出：")
print(company)  # 输出: tom,bob,jane

# 在解释器中直接输入变量名会调用__repr__方法
print("\nrepr(company) 输出：")
print(repr(company))  # 输出: tom,bob,jane

# 如果没有定义__repr__，默认输出如：<__main__.Company object at 0x1006de518>
'''
总结：

1. __repr__ 是开发模式下用的，用于调试和日志记录
2. __str__ 是对对象进行字符串格式化的时候调用的，面向用户
3. 如果只能实现一个，优先实现__repr__
4. 实际开发中，通常两个都会实现，提供不同场景下的字符串表示
'''