#! -*- encoding=utf-8 -*-

# mixin模式特点
'''
1、mixin类功能单一
2、mixin不和基类关联，可以合任何基类组合，基类可以不和mixin进行关联就能初始化成功
3、mixin中不要使用super这种用法，因为super是根据__mro__的顺序来找，
又不和基类关联，所以意义不大还容易出错
'''