# 《Python编程：从入门到实践》
Python_preToPractice

---

- [函数](#函数)
    - [规范](#规范)
    - [默认值](#默认值)
    - [title()](#title)
    - [实现实参可选](#实现实参可选)
    - [禁止函数修改列表](#禁止函数修改列表)


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


<a id = "默认值"></a>
### 默认值：

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
### title()

处理首字母大写，字符串可以调用。


<a id = "实现实参可选"></a>
### 实现实参可选

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


<a id = "禁止函数修改列表"></a>
### 禁止函数修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。

若要禁止，可以利用**切片技巧**：
**切片表示法`[:]`创建列表的副本**。比如：

```
def list_exampla(names[:],ages):
    '''处理姓名和年龄列表'''
    print "this is a example!"
```

这个函数处理的就是names这个列表的副本，而不是names列表的本身。

**注意：**

虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，
否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创
建副本，从而提高效率，在处理大型列表时尤其如此。

