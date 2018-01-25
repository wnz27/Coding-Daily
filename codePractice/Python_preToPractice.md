# 《Python编程：从入门到实践》
Python_preToPractice

---

- [函数](#函数)
    - [规范](#规范)
    - [传递参数](#传递参数)
        - [默认值](#默认值)
        - [title()](#title)
        - [实现实参可选](#实现实参可选)
    - [传递列表](#传递列表)
        - [禁止函数修改列表](#禁止函数修改列表)
        - [传递任意数量的实参](#传递任意数量的实参)
        - [使用任意数量的关键字实参](#使用任意数量的关键字实参)


<a id = "函数"></a>
## 函数


<a id = "规范"></a>
### 规范：

函数名底下用三个单引号的注释，告知看源码的人该函数的作用。

```
def favoriate_book(title):
    '''显示最喜欢的书籍的函数！'''
    print "One of my favoriate book is %s!" %title
```

<a id = "传递参数"></a>
### 传递参数

<a id = "默认值"></a>
#### 默认值：

定义函数的时候，可以给每个形参指定默认值。当我们给实参的时候，函数将使用指定的实参，当我们不给实参的时候，函数使用默认值。

**注意**：

使用默认值时，在形参列表中必须 _先列出没有默认值的形参，再列出有默认值的实参_ 。比如：

```
def animals(a_name, a_type = "dog"):
    '''显示宠物信息'''
    print "I have a " + a_type + ", It name is " + a_name +"!"

animals("cat","dada")
animals("duo")
```


<a id ="title"></a>
#### title()

处理首字母大写，字符串可以调用。


<a id = "实现实参可选"></a>
#### 实现实参可选

可以用**空字符**实现实参可选，比如：

```
def get_format_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_format_name("little1","little2")
print musician

musician = get_format_name("big1","big2","big3")
print musician
```

<a id = "传递列表"></a>
### 传递列表

<a id = "禁止函数修改列表"></a>
#### 禁止函数修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。

若要禁止，可以利用**切片技巧**：
**切片表示法`[:]`创建列表的副本**。比如：

```
names = ["aaaaaa","bbbbb","ccccc"]
def list_exampla(names,ages):
    '''处理姓名和年龄列表'''
    for name in names:
        names.pop()
        print names
    print "this is a example!"
list_exampla(names[:],18)
print names
```

这个函数处理的就是names这个列表的副本，而不是names列表的本身。

**注意：**

虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，
否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创
建副本，从而提高效率，在处理大型列表时尤其如此。


<a id = "传递任意数量的实参" ></a>
#### 传递任意数量的实参

若你预先不知道函数将会处理多少实参，Python的函数调用可以收集任意数量的实参来满足这种需求。比如：

```
def make_pizza(*toppings):
    print toppings
make_pizza("a")
make_pizza("b","c")
```

形参名`*toppings`中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。

函数体内的print语句通过生成输出来证明Python能够处理 使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形。

它以类似的方式处理不同的调用，注意，Python将实参封装到一个**元组**中，即便函数只收到一个值也如此，会输出这样：
```
('a',)
('b', 'c')
```

我们可以配合for语句进行遍历输出，但注意生成元组时是无序的。


<a id = "使用任意数量的关键字实参"></a>
#### 使用任意数量的关键字实参

有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。

在这种情况下，可将函数编写成能够接受**任意数量的键—值对**——调用语句提供了多少就接受多少。

一个这样的示例是创建用户简介:你知道你将收到有关用户的信息，但不确定会是什么样的信息。
在下面的示例中，函数接受名和姓，同时还接受**任意数量**的关键字实参:

```
def build_profile(first,last,**user_info):
    '''创建字典，包含用户信息！'''
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile("aaaa","bbbb",gender = "male",age = "18")
print user_profile
```

函数的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—值对。

形参`**user_info`中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中。

在这个函数中，可以像访问其他字典那样访问user_info中的名称—值对。

以上例子打印结果为：
```
{'gender': 'male', 'first_name': 'aaaa', 'last_name': 'bbbb', 'age': '18'}
```

编写函数时，你可以以各种方式混合使用位置实参、关键字实参和任意数量的实参。
知道这些实参类型大有裨益，因为阅读别人编写的代码时经常会见到它们。
要正确地使用这些类型的实参并知道它们的使用时机，需要经过一定的练习。
