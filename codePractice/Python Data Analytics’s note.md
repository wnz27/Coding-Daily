# 《数据分析实战》笔记--Python Data Analytics’s note
Python Data Analytics’s note

---

- [函数式编程简单探索](#函数式编程简单探索)





---
<a id = 函数式编程简单探索></a>
## 函数式编程简单探索

应尽量避免显示循环，Python提供了几种方法，诸如函数式编程（functional programing，亦即expression—oriented programing，面向表达式的编程）等编程技巧。

Python提供的用于函数式编程开发的函数有：

* `map(function,list)`，映射函数
* `filter(function,list)`，过滤函数
* `reduce(functiong,list)`，规约函数
* `lambda`函数
* 列表生成器

`for`语句循环对每个元素执行某一操作，然后把结果汇集起来，其实同样的功能可以用`map()`函数实现：
```
items = [1,2,3,4,5]
def inc(x):
    return x + 1

print(list(map(inc,items)))
# 输出为 [2, 3, 4, 5, 6]
```
先定义一个对每一个元素操作的函数，在这里是`inc（）`，然后把它作为`map()`的第一个参数传进去，

Python允许把`lambda`函数直接用在第一个参数的位置来定义函数，这样能大幅精简代码：
```
print(list(map(lambda x : x + 1, items)))
```
其他两个函数`filter（）`和`reduce（）`工作原理类似。

- `filter（）`函数只抽取函数返回值为`True`的列表元素。
- `reduce（）`函数对列表所有元素依次计算后返回唯一结果。使用`reduce（）`前要导入`functools`模块。

例子：
```
from functools import reduce
print(list(filter(lambda x : x <4 , items))) # 过滤出比4小的数
print(reduce(lambda x,y : x/y , items)) # 对列表从第一个数依次计算前一个除以后一个
```
filter应该不需要解释了。解释一下`reduce（）`：

`items`中是，1，2，3，4，5。这个函数就是计算：(((1/2)/3)/4)/5。

函数式编程最后一个概念，列表生成式（`list comprehension`）。

这个概念可以用来以非常自然和简单的方式来创建列表，而这种创建方式跟数学家描述数据集所使用的类似。列表这个序列所包含的元素由特定的函数和运算来指定：
```
s = [x**2 for x in range(5)]
print(s)
# 输出: [0, 1, 4, 9, 16]
```






