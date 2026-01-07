#! -*- encoding=utf-8 -*-
# Python自定义可切片对象 - 实现sequence协议

'''
实现可切片对象需要的魔法方法：

1. 必须实现的方法：
   - __getitem__(self, item): 实现索引和切片访问
   - __len__(self): 返回长度

2. 可选实现的方法：
   - __iter__(self): 实现迭代
   - __contains__(self, item): 实现in运算符
   - __reversed__(self): 实现反向迭代

3. 本例特点：
   - 实现了不可修改序列（sequence）
   - 支持切片操作
   - 支持迭代和成员检测
'''

import numbers

print("=" * 50)
print("自定义可切片对象实现")
print("=" * 50)

class Group:
    """组类 - 演示如何实现一个支持切片的对象
    
    实现了不可修改序列协议，支持：
    - 索引访问：group[0]
    - 切片访问：group[1:3]
    - 长度：len(group)
    - 迭代：for item in group
    - 成员检测：item in group
    - 反向迭代：reversed(group)
    """
    
    def __init__(self, group_name, company_name, staffs):
        """初始化组对象
        
        Args:
            group_name: 组名
            company_name: 所属公司名
            staffs: 员工列表
        """
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs
    
    def __reversed__(self):
        """实现反向迭代
        
        Note:
            - reversed(group)会调用此方法
            - 这里直接修改了staffs列表
        """
        self.staffs.reverse()
    
    def __getitem__(self, item):
        """实现索引和切片访问
        
        Args:
            item: 索引或切片对象
            
        Returns:
            Group: 返回新的Group对象
            
        Note:
            - 支持两种类型的item：
              1. slice对象：group[1:3]
              2. 整数：group[0]
            - 都返回Group对象，保持类型一致性
        """
        cls = type(self)  # 获取当前类
        
        if isinstance(item, slice):
            # 处理切片：group[1:3]
            return cls(
                group_name=self.group_name,
                company_name=self.company_name,
                staffs=self.staffs[item]  # 切片操作
            )
        elif isinstance(item, numbers.Integral):
            # 处理整数索引：group[0]
            return cls(
                group_name=self.group_name,
                company_name=self.company_name,
                staffs=[self.staffs[item]]  # 单个元素也放入列表
            )

    def __len__(self):
        """返回序列长度
        
        Returns:
            int: 员工数量
            
        Note:
            - len(group)会调用此方法
        """
        return len(self.staffs)
    
    def __iter__(self):
        """返回迭代器
        
        Returns:
            iterator: staffs列表的迭代器
            
        Note:
            - for循环会调用此方法
            - 直接返回staffs的迭代器
        """
        return iter(self.staffs)
    
    def __contains__(self, item):
        """实现成员检测
        
        Args:
            item: 要检测的元素
            
        Returns:
            bool: 是否包含该元素
            
        Note:
            - 'item in group'会调用此方法
        """
        if item in self.staffs:
            return True
        else:
            return False
    
# 创建组对象
print("\n创建组对象...")
staffs = ["fzk1", "fzk2", "fzk3", "fzk4"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)

# 测试切片
print("\n" + "=" * 50)
print("测试切片操作")
print("=" * 50)
a = group[:2]  # 调用__getitem__并传入slice对象
print(f"group[:2].staffs = {a.staffs}")  # ['fzk1', 'fzk2']

# 测试长度
print(f"\nlen(group) = {len(group)}")  # 4

# 测试成员检测
print("\n" + "=" * 50)
print("测试成员检测 (in 运算符)")
print("=" * 50)
if "fzk1" in group:  # 调用__contains__
    print("'fzk1' 在组中")

# 测试迭代
print("\n" + "=" * 50)
print("测试迭代 (for 循环)")
print("=" * 50)
for user in group:  # 调用__iter__
    print(f"  - {user}")

# 测试反向迭代
print("\n" + "=" * 50)
print("测试反向迭代 (reversed)")
print("=" * 50)
reversed(group)  # 调用__reversed__
for user in group:
    print(f"  - {user}")

print("\n" + "=" * 50)
print("总结")
print("=" * 50)
print("""
实现自定义序列类的关键点：

1. 必须实现的方法：
   - __getitem__: 实现索引和切片访问
   - __len__: 返回序列长度

2. 增强功能的方法：
   - __iter__: 使for循环更高效
   - __contains__: 支持in运算符
   - __reversed__: 支持reversed()函数

3. __getitem__的实现技巧：
   - 使用isinstance判断是slice还是整数
   - 使用numbers.Integral而不是int（兼容性更好）
   - 返回同类型对象，保持API一致性

4. 应用场景：
   - 自定义集合类
   - 数据容器类
   - 代理对象
   - 惰性加载序列
""")