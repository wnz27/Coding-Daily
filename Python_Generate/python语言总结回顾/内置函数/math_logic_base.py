'''
官方文档中介绍函数的说明,比如：
max(iterable,*[, key, default])
max 函数的几个形参，为什么有 * 符号，又有 []？
函数形参列表中符号 * 表示，后面的形参只能为关键字参数（keyword argument），
不能为位置参数（positional argument），也就是说，max 函数要这么用：
'''
a = [1,2,3,4,2,2,3]
print(max(a,key=lambda x: a.count(x), default=1))
# 比如我们定义一个函数func，参数 b 位于 * 后面，只能为关键字参数：
def func(a, *, b):
    pass

func(2,b=1)  # 不会报错
'''func(2, 1)
会报错：
TypeError: func() takes 1 positional argument but 2 were given
'''
