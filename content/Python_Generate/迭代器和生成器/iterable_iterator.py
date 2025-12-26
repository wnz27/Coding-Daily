#! -*- encoding=utf-8 -*-
# 演示Python中的可迭代对象（Iterable）和迭代器（Iterator）的区别和实现

from collections.abc import Iterator, Iterable

class Company(object):
    """公司类 - 演示可迭代对象的实现
    
    实现了__iter__方法，使其成为可迭代对象。
    """
    
    def __init__(self, employee_list):
        """初始化公司对象
        
        Args:
            employee_list: 员工列表
        """
        self.employee = employee_list
    
    def __iter__(self):
        """返回一个迭代器对象
        
        Returns:
            MyIterator: 自定义的迭代器对象
            
        Note:
            - 这个方法必须返回一个迭代器对象（实现了__next__方法）
            - 如果返回其他类型，会报错：TypeError: iter() returned non-iterator
        """
        # 这里如果返回return 1，会报错：
        # TypeError: iter() returned non-iterator of type 'int'
        return MyIterator(self.employee)

    # 可选方案：使用__getitem__方法
    # def __getitem__(self, item):
    #     """通过索引访问元素
    #     
    #     如果实现了__getitem__，即使没有__iter__，
    #     for循环也可以工作（Python会自动使用索引迭代）
    #     """
    #     return self.employee[item]

class MyIterator(Iterator):
    """自定义迭代器类
    
    继承自Iterator抽象基类，只需要实现__next__方法。
    Iterator已经实现了__iter__方法（返回self）。
    
    Note:
        迭代器协议需要实现两个方法：
        1. __iter__(): 返回迭代器对象自身
        2. __next__(): 返回下一个值，没有值时抛出StopIteration
    """
    
    def __init__(self, employee_list):
        """初始化迭代器
        
        Args:
            employee_list: 要迭代的元素列表
        """
        self.iter_list = employee_list
        self.index = 0  # 当前迭代位置

    def __next__(self):
        """返回下一个元素
        
        Returns:
            当前位置的元素
            
        Raises:
            StopIteration: 当没有更多元素时抛出
            
        Note:
            这是迭代器的核心方法，实现真正的迭代逻辑
        """
        try:
            word = self.iter_list[self.index]
        except IndexError:
            # 当索引超出范围时，抛出StopIteration异常
            raise StopIteration
        self.index += 1
        return word

if __name__ == "__main__":
    print("=" * 50)
    print("演示迭代器的使用")
    print("=" * 50)
    
    # 创建公司对象（可迭代对象）
    company = Company(["fzk", "fzk1", "fzk2"])
    
    # 方法1：手动使用iter()和next()
    print("\n方法1：手动调用next()")
    my_itor = iter(company)  # 调用__iter__方法，获取迭代器
    while True:
        try:
            employee = next(my_itor)  # 调用__next__方法
            print(f"员工: {employee}")
        except StopIteration:
            print("迭代结束")
            break

    # 方法2：使用for循环（推荐）
    print("\n方法2：使用for循环")
    for item in company:
        print(f"员工: {item}")
    
    print("\n" + "=" * 50)
    print("可迭代对象 vs 迭代器")
    print("=" * 50)
    print("""
    可迭代对象（Iterable）：
    - 实现了__iter__方法的对象
    - 可以被迭代，但自身不是迭代器
    - 例如：list, tuple, str, dict, set等
    - 每次调用iter()都会返回一个新的迭代器
    
    迭代器（Iterator）：
    - 同时实现了__iter__和__next__方法的对象
    - 本身就是迭代器，也是可迭代对象
    - __iter__方法返回自身
    - __next__方法返回下一个值，没有更多值时抛出StopIteration
    - 迭代器是一次性的，迭代完后就不能再次使用
    
    关系：
    - 所有迭代器都是可迭代对象
    - 但不是所有可迭代对象都是迭代器
    """)
