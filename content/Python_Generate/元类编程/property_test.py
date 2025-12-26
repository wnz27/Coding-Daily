#! -*- encoding=utf-8 -*-
# Python的@property装饰器详解 - 将方法转换为属性访问

'''
@property装饰器的作用：

1. 主要作用：
   - 将方法转换为属性，使用更自然
   - 可以在获取/设置值时添加逻辑检查
   - 实现计算属性（根据其他属性动态计算）

2. 使用方式：
   - @property: 定义getter方法（只读）
   - @attr.setter: 定义setter方法（可写）
   - @attr.deleter: 定义deleter方法（可删）

3. 优点：
   - 代码更Pythonic，更符合Python风格
   - 可以在不修改外部接口的情况下添加逻辑
   - 实现数据封装和验证
'''

from datetime import date, datetime

class User:
    """用户类 - 演示@property的使用"""
    
    def __init__(self, name, birthday):
        """初始化用户
        
        Args:
            name: 用户名
            birthday: 生日（date对象）
        """
        self.name = name
        self.birthday = birthday
        self._age = 0  # 私有属性，存储手动设置的年龄
    
    # 传统方式：使用方法获取年龄
    # def get_age(self):
    #     """获取用户年龄"""
    #     return datetime.now().year - self.birthday.year
    # 缺点：需要用 user.get_age() 调用，不够自然

    @property
    def age(self):
        """计算年龄属性 - 使用@property装饰器
        
        Returns:
            int: 用户年龄
            
        Note:
            - 使用@property后，可以像访问属性一样访问：user.age
            - 这是一个计算属性，每次访问都会重新计算
            - getter方法：定义读取属性时的行为
        """
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        """设置年龄 - 使用@age.setter装饰器
        
        Args:
            value: 要设置的年龄值
            
        Note:
            - setter方法：定义设置属性时的行为
            - 可以在这里添加数据验证逻辑
            - 例如：验证年龄是否合理（0-150）
        """
        # 这里可以添加验证逻辑
        # if not 0 <= value <= 150:
        #     raise ValueError("年龄必须在0-150之间")
        self._age = value

if __name__ == "__main__":
    print("=" * 50)
    print("@property装饰器使用示例")
    print("=" * 50)
    
    # 创建用户对象
    user = User("fzk", date(year=1992, month=1, day=1))
    
    # 方式1：使用方法（已注释）
    # print(user.get_age())  # 需要加()调用
    
    # 方式2：使用@property（推荐）
    print(f"计算得到的年龄: {user.age}")  # 像访问属性一样，不需要()
    
    # 使用setter设置年龄
    user.age = 40
    print(f"手动设置的年龄: {user.age}")  # 这里读取的是计算值，不是_age
    print(f"私有属性_age: {user._age}")  # _age存储了手动设置的值
    
    print("\n" + "=" * 50)
    print("@property总结")
    print("=" * 50)
    print("""
    @property的优势：
    
    1. 使用更自然：
       - 旧: user.get_age()  # 看起来像方法调用
       - 新: user.age        # 看起来像属性访问
    
    2. 封装计算逻辑：
       - 可以将复杂的计算封装在属性后面
       - 外部代码不需要知道内部实现
    
    3. 数据验证：
       - setter中可以添加数据验证逻辑
       - 防止无效数据设置
    
    4. 兼容性好：
       - 可以将现有属性改为property，不需修改调用代码
       - API保持不变，但内部实现可以更灵活
    
    5. 应用场景：
       - 计算属性（如年龄、BMI、全名等）
       - 属性验证（如邮箱格式、年龄范围）
       - 延迟加载（首次访问时才加载数据）
       - 缓存结果（避免重复计算）
    """)
