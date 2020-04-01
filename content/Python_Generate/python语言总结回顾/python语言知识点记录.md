## Python语言特性

### 进程、线程、GIL
- [一文讲清线程与GIL](https://github.com/wnz27/self-article/blob/master/content/%E6%8A%80%E6%9C%AF%E6%9D%82%E7%AF%87/python%E7%9B%B8%E5%85%B3/GIL%E8%BF%9B%E7%A8%8B%E4%BB%A5%E5%8F%8A%E7%BA%BF%E7%A8%8B.md)

### 动态语言
讲动态与静态之前先清楚什么叫类型检查，
类型检查是验证类型约束的过程，**编译器或解释器通常在编译阶段或运行阶段**做类型检查。
类型检查就是查看“变量”和它们的”类型”，然后判断表达式是否合理。
例如，不能拿一个 string 类型变量除以浮点数变量。

如果类型检查发生在程序**运行阶段（run time）**，那么它便是“动态类型语言”（dynamically typed languages）。
常见的动态语言包括：
- Python
- JavaScrpit
- PHP
类型检查发生在**编译阶段（compile time）**的是“静态类型语言”（statically typed languages）。
常见的静态类型语言包括：
- C
- C++
- Java
- C#
- Scala

### 强类型语言
强类型语言是指：不管是在编译阶段还是运行阶段，一旦某种类型绑定到变量后，
此变量便会持有此类型，并且不能同其他类型在计算表达式时，混合使用。
常见的强类型语言有：
- Python
- Java
- C#
- Scala

弱类型语言容易与其他类型混合计算。弱类型语言代表 JavaScript。
```
var data = 100
data = data + 'zhangsan' //string 和 int 结合自动转化为 string
```
以上会输出`100zhangsan`

常见的弱类型语言有：
- C
- C++
- PHP 
- Javascript

## Python中可变与不可变类型
不可变：
- bool
- int
- float
- tuple
- str
- frozenset

可变：
- list
- set
- dict

## Python中的深浅拷贝
直接赋值，是浅拷贝
使用`copy()`是深拷贝
浅拷贝之后改变浅拷贝的值，原被拷贝变量受影响
深拷贝之后改变深拷贝的值，与原拷贝变量没有关系。

## 异常处理
在编写程序时通常会遇到两种错误。
1. 第一种是语法错误，也就是说，程序员在编写语句或者表达式时出错。
例如，在写for语句时忘记加冒号。
```
>>> for i in range(10)
SyntaxError: invalid syntax (<pyshell#61>, line 1)
```
在这个例子中，Python解释器发现，由于语句不符合Python语法规范，因此它无法执行这条指令。

2. 第二种是逻辑错误，即程序能执行完成但返回了错误的结果。
这可能是由于算法本身有错，或者程序员没有正确地实现算法。
有时，逻辑错误会导致诸如除以0、越界访问列表等非常严重的情况。
这些逻辑错误会导致运行时错误，进而导致程序终止运行。
通常，这些运行时错误被称为异常。

许多程序员简单地把异常等同于引起程序终止的严重运行时错误。
然而，大多数编程语言都提供了让程序员能够处理这些错误的方法。
此外，程序员也可以在检测到程序执行有问题的情况下自己创建异常。

当异常发生时，我们称程序“抛出”异常。可以用try语句来“处理”被抛出的异常。
例如，以下代码段要求用户输入一个整数，然后从数学库中调用平方根函数。
如果用户输入了一个大于或等于0的值，那么其平方根就会被打印出来。
但是，如果用户输入了一个负数，平方根函数就会报告ValueError异常。
```
>>> anumber = int(input("Please enter an integer "))
Please enter an integer -23
>>> print(math.sqrt(anumber))
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print(math.sqrt(anumber))
ValueError: math domain error
```
可以在try语句块中调用print函数来处理这个异常。
对应的except语句块“捕捉”到这个异常，并且为用户打印一条提示消息。
```
>>> try:
       print(math.sqrt(anumber))
    except:
       print("Bad Value for square root")
       print("Using absolute value instead")
       print(math.sqrt(abs(anumber)))

Bad Value for square root
Using absolute value instead
4.79583152331
```
except会捕捉到sqrt抛出的异常并打印提示消息，然后会使用对应数字的绝对值来保证sqrt的参数非负。
这意味着程序并不会终止，而是继续执行后续语句。

程序员也可以使用raise语句来触发运行时异常。
例如，可以先检查值是否为负，并在值为负时抛出异常，而不是给sqrt函数提供负数。
下面的代码段显示了创建新的RuntimeError异常的结果。
注意，程序仍然会终止，但是导致其终止的异常是由我们自己手动创建的。
```
>>> if anumber < 0:
...    raise RuntimeError("You can't use a negative number")
... else:
...    print(math.sqrt(anumber))
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
RuntimeError: You can't use a negative number
```
除了RuntimeError以外，还可以抛出很多不同类型的异常。


## 数据类型总结

#### print
格式化运算符的右边是将被插入格式化字符串的一些值。这个集合可以是元组或者字典。

如果这个集合是元组，那么值就根据位置次序被插入。也就是说，元组中的第一个元素对应于格式化字符串中的第一个格式化字符。

如果这个集合是字典，那么值就根据它们对应的键被插入，并且所有的格式化字符必须使用(name)修改符来指定键名。
```
>>> price = 24
>>> item = "banana"
>>> print("The %s costs %d cents" % (item,price))
The banana costs 24 cents
>>> print("The %+10s costs %5.2f cents" % (item,price))
The     banana costs 24.00 cents
>>> print("The %+10s costs %10.2f cents" % (item,price))
The     banana costs     24.00 cents
>>> itemdict = {"item":"banana","cost":24}
>>> print("The %(item)s costs %(cost)7.1f cents" % itemdict)
The banana costs    24.0 cents
```

###  容器类数据类型
* [list 和 tuple 使用小案例](./list和tuple/list_tuple_example.py)
* [dict 和 set基本操作](./dict和set/dict_set_basic.py)
* [dict 和 set 使用小案例](./dict和set/dict_set_example.py)
* [数学运算、逻辑运算以及进制转化相关内置函数](./内置函数/math_logic_base.py)

## 其他
#### 转义字符表

转义字符|描述|转义字符|描述
-:|:-:|:-:|:-
\\|续行符|\b|退格
\\\\|反斜杠符号|\e|转义
\\'|单引号|\000|空
\\''|双引号|\v|纵向制表符
\a|响铃|\r|回车
\t|横向制表符|\n|换行符

## 进阶
### 协程
- [协程学习笔记 --《流畅的python》](./协程（流畅的python学习）/协程学习.md)


