'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-19 12:04:56
@LastEditTime: 2020-03-20 05:14:45
@FilePath: /Coding-Daily/self-problem/习题1/p2.py
@description: type some description
'''
'''
2. 请实现一个 Python 方法：输入一个路径，动态加载目录内的所有模块
定义一个方法接受一个path, 导入所有模块？
'''
import importlib, os, sys

def my_import_from_path(module_path):
    """
    type: str
    rtype: None
    description: 根据路径动态加载目录内所有的模块
    """
    # 把module_path加入系统路径
    sys.path.append(module_path)
    # 列出module_path底下所有文件名：
    file_name_list = os.listdir(module_path)
    print(file_name_list)
    # 使用自定义函数格式化文件名去掉后缀以及过滤不是包的东西
    module_name_list = __format_filename_to_module_name(file_name_list)
    print(module_name_list)
    for package_name in module_name_list:
        tem = importlib.import_module(".", package_name)
        print(dir(tem))
def __format_filename_to_module_name(file_list):
    '''
    type: file list, list[str]
    rtype: module_name_list, list[str]
    description: 格式化文件名去掉后缀，且过滤掉不是.py的文件，
    还去掉除了后缀有点的文件
    '''
    res = []
    for file in file_list:
        if file.endswith(".py") and "." not in file[:-3]:
            res.append(file[:-3])
    return res

# 测试一下
path1 = '/Users/fzk27/fzk27/Coding-Daily/DesignPattern/Python设计模式/相关代码/第一章'
my_import_from_path(path1)

    