'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-19 11:51:18
@LastEditTime: 2020-03-20 04:49:03
@FilePath: /Coding-Daily/self-problem/testtesttest哈哈哈/attempt.py
@description: type some description
'''
# import threading
# def test(h):
#     print("adfadf", h)

# threading.Thread(target=test, args=("123",)).start()
# from lib import A,B
__author__ = "27"

class ClassA:
    def test(self):
        print('test')

    int_value = 1
    str_value = __author__

# 全局方法，加载时会被调用
print(__file__, 'global function.')

if __name__ == '__main__':
    print(__file__, __name__)

# 注意：模块名不包括.py后缀
imp_module = 'test'
imp_class = 'ClassA'

# 使用importlib
# importlib相比__import__()，操作更简单、灵活，支持reload()
import importlib
ip_module = importlib.import_module('.', imp_module)
ip_module_cls = getattr(ip_module, imp_class)
cls_obj = ip_module_cls()
if 'int_value' in dir(cls_obj):
    print(cls_obj.int_value)
    cls_obj.int_value = 10
    print(cls_obj.int_value)

# reload()重新加载，一般用于原模块有变化等特殊情况。
# reload()之前该模块必须已经使用import导入模块。
# 重新加载模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块，reload后还是用原来的内存地址。
ip_module = importlib.reload(ip_module)
print(getattr(ip_module, imp_class).int_value)

# 循环多次加载相同文件，手动修改文件数据，发现重新加载后输出内容变更。
# from time import sleep
# for i in range(30):
#     ip_module = importlib.reload(ip_module)
#     print(getattr(ip_module, imp_class).int_value)
#     sleep(3)
