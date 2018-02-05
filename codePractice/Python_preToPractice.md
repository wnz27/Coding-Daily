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
    - [将函数存储在模块中](#将函数存储在模块中)
        - [导入整个模块](#导入整个模块)
        - [导入特定函数](#导入特定函数)
        - [使用as给函数指定别名](#用as给函数指定别名)
        - [使用as给模块指定别名](#用as给模块指定别名)
        - [导入模块中的所有函数](#导入模块中的所有函数)
    - [函数编写指南](#函数编写指南)
- [类](#类)
    - [创建类和使用类](#创建类和使用类)
        - [创建类](#创建类)
        - [根据类创建实例](#根据类创建实例)
        - [访问属性](#访问属性)
        - [调用方法](#调用方法)
        - [创建多个实例](#创建多个实例)
    - [使用类和实例](#使用类和实例)
        - [car类](#car类)
        - [给属性指定默认值](#给属性指定默认值)
        - [修改属性的值](#修改属性的值)
            - [1、直接通过实例进行修改](#直接通过实例进行修改)
            - [2、通过方法进行设置](#通过方法进行设置)
            - [3、通过方法进行递增](#通过方法进行递增)
    - [继承](#继承)
        - [子类的方法__init__()](#子类的方法)
        - [给子类定义属性和方法](#给子类定义属性和方法)
        - [重写父类的方法](#重写父类的方法)
        - [将实例用作属性](#将实例用作属性)
        - [hahah]()
        
        
        
---
<a id = "函数"></a>
## 函数

---

<a id = "规范"></a>
### 规范：

函数名底下用三个单引号的注释，告知看源码的人该函数的作用。

```
def favoriate_book(title):
    '''显示最喜欢的书籍的函数！'''
    print "One of my favoriate book is %s!" %title
```

当然，还可以在程序段任意位置加入注释以让浏览你程序的人更快速明白你的意图。


---
<a id = "传递参数"></a>
### 传递参数

<a id = "默认值"></a>
#### 默认值：

定义函数的时候，可以给每个形参指定默认值。当我们给实参的时候，函数将使用指定的实参，当我们不给实参的时候，函数使用默认值。

**注意**：

使用默认值时，在形参列表中必须**先列出没有默认值的形参，再列出有默认值的实参**。比如：

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

---
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

---
<a id = "将函数存储在模块中"></a>
### 将函数存储在模块中 

函数的优点之一是，使用它们可将代码块与主程序分离。

通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。
`import`语句允许在当前运行的程序文件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。

将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

<a id ="导入整个模块"></a>
#### 导入整个模块

比如你在`test.py`这个文件里写python程序，你想保证你这个文件里的代码简洁清晰，想把函数写在另一个文件里，这是可以的。
最简单初始的方法就是整体导入。

1. 在与`test.py`**相同的文件夹(同一目录)**里创建一个python文件（后缀为py的文件），用于写函数。

2. 比如你这个用于写函数的文件名称为`testFun.py`，你在里面定义了这样一个函数：
```
def test_print(some_message):
    '''打印传入的信息'''
    print some_message 
```

3. 导入整个模块的方法是，你在`test.py`文件中用整体导入语句：
```
import testFun #使用需要导入的文件名，进行整体导入
testFun.test_print("abc") #直接用导入的文件名，然后点语法+函数名就可直接使用。
```

<a id ="导入特定函数"></a>
#### 导入特定函数

* 方法是使用这样形式的语句：`from module_name import function_name`

还拿上面的例子说，我先把`testFun.py`文件加一个函数：
```
def test_print(some_message):
    '''打印传入的信息'''
    print some_message
def test_another_print(some_message):
    '''打印另一条传入的信息'''
    print "Another " + some_message
```

这时候你在`test.py`文件中使用上面给出的形式：
```
from testFun import test_another_print #调用testFun模块中的test_another_print
testFun.test_print("abc")  #错误语句
test_another_print("aaaa") #正确语句
```

如果你还留着上面整体导入的调用函数的语句，Python会给你报这样一个错误：
```
NameError: name 'testFun' is not defined
```

意思是testFun这个没有被定义。

或者如果你调用第一个函数：
```
test_print("abc") #这个语句是正确的
```

但它也会给你报错：
```
NameError: name 'test_print' is not defined
```

也是告诉你test_print，没有定义。你会觉得明明在写函数的文件里了啊。

造成这两个问题的原因相同：
**因为这个导入函数的语法只导入特定的函数，只能调用导入的函数，不能使用未导入的函数，
并且只需要函数名即可，也不需要像导入整体一样使用模块名和点语法。**

* 看到这你们也许会有疑问，一次只导入一个函数岂不效率低下？Python是考虑到这个问题的，所以有多函数一起导入的方法：
```
from module_name import function_name1，function_name2, function_name3
```

把函数名用逗号隔开即可。


<a id = "用as给函数指定别名"></a>
#### 使用`as`给函数指定别名

如果要导入的函数的名称**可能与程序中现有的名称冲突**，或者函数的名称太长，可指定简短而独一无二的别名 ——函数的另一个名称，类似于外号。
要给函数指定这种特殊外号，需要在导入它时这样做：
`from module_name import function_name as fn`

这个`fn`就是外号，这时候调用函数的时候使用外号就行。再用上面的例子：
```
from testFun import test_another_print as t_a_p #给函数指定别名t_a_p
t_a_p("aaaaa") #这时别名就生效了
```
这时你再用：`test_another_print（"aaaaa"）`也会报`NameError`的错误。
意味着指定别名之后只能用别名来调用函数。


<a id = "用as给模块指定别名"></a>
#### 使用`as`给模块指定别名

与给函数指定别名类似，只需这个语句即可：
```
import module_name as mn
```

这个mn就是模块的别名，所以这时候与导入整体的调用类似，只不过把模块名称换成别名即可，函数还是用点语法来调用。

**好处**：

这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。
这些函数名明确地指出了函数的功能，对理解代码而言，它们 比模块名更重要。


<a id = "导入模块中所有函数"></a>
#### 导入模块中的所有函数

使用星号`*`运算符可让Python导入模块中的所有函数:
```
from testFun import * #从testFun模块导入所有的函数
```

`import`语句中的星号让Python将模块`testFun`中的每个函数都复制到这个程序文件中。
由于导入了每个函数，可通过**函数名称**来调用每个函数，而**无需使用句点表示法**。

然而，使用并非自己编写的**大型模块**时，最好不要采用这种导入方法。
如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
*Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。*

**最佳**的做法是，要么只导入你**需要使用的函数**，要么导入**整个模块并使用句点表示法**。这能让代码更清晰，更容易阅读和理解。


<a id = "函数编写指南"></a>
### 函数编写指南

* 应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。

* 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它:
*他们完全可以相信代码如描述的那样运行，只要知道函数的名称、需要的实参以及返回值的类型，就能在自己的程序中使用它。*

* 给形参指定默认值时，等号两边不要有空格:
```
def function_name(parameter_0, parameter_1="default value")
```

* 对于函数调用中的关键字实参，也应遵循这种约定:
```
 function_name(value_0, parameter_1="value")
```

* 如果形参过长，单行放不下，可以灵活的运用回车和空格来把形参放成一种清晰的形式，区分开函数体。比如:
```
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5)：
    function body... 
```

* 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。

* 所有的`import`语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。

**简单小结：**

* 函数让你编写代码一次后，想重用它们多少次就重用多少次。需要运行函数中的代码时，只需编写一行函数调用代码，就可让函数完成其工作。
需要修改函数的行为时，只需修改一个代码块，而所做的修改将影响调用这个函数的每个地方。

* 使用函数让程序更容易阅读，而良好的函数名概述了程序各个部分的作用。相对于阅读一系列的代码块，阅读一系列函数调用让你能够更快地明白程序的作用。

* 函数让代码更容易测试和调试。如果程序使用一系列的函数来完成其任务，而其中的每个函数都完成一项具体的工作，测试和维护起来将容易得多：
*你可编写分别调用每个函数的程序，并测试每个函数是否在它可能遇到的各种情形下都能正确地运行。*


---
<a id = "类"></a>
## 类

面向对象编程 是最有效的软件编写方法之一。在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。

根据类来创建对象被称为实例化 ，这让你能够使用类的实例。你可以指定可在实例中存储什么信息，定义可对这些实例执行哪些操作。
你还可以编写一些类来扩展既有类的功能，让相似的类能够高效地共享代码。

你可以把自己编写的类存储在模块中，并在自己的程序文件中导入其他程序员编写的类。理解面向对象编程有助于你像程序员那样看世界，
还可以帮助你真正明白自己编写的代码，不仅是各行代码的作用，还有代码背后更宏大的概念。
了解类背后的概念可培养逻辑思维，让你能够通过编写程序来解决遇到的几乎任何问题。
类还能让你以及与你合作的其他程序员基于同样的逻辑来编写代码，你们就能明白对方所做的工作。


---
<a id = "创建类和实用类"></a>
### 创建类和使用类

使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类，它表示的不是特定的小狗，而是任何小狗。对于大多数宠物狗，我们都知道些什么呢?
它们都有名字 和年龄;我们还知道，大多数小狗还会蹲下和打滚。
由于大多数小狗都具备上述两项信息(名字和年龄)和两种行为(蹲下和打滚)，我们的Dog类将包含它们。这个类让 Python知道如何创建表示小狗的对象。

编写这个类后，我们将**使用**它来创建表示特定小狗的实例。


<a id = "创建类"></a>
#### 创建类

我们以创建一个狗的类为列子，狗狗会有`名字`和`年龄`这**两项信息**，以及`蹲下`和`打滚`这**两项行为**，我们用类来实现它们：
```
class Dog():                         #1、定义类
    '''一次模拟小狗类的尝试'''
    def __init__(self,name,age):     #2、__init__方法
        '''初始化名称和年龄'''
        self.name = name             #3、前缀self
        self.age = age
    
    def sit(self):                   #4、行为方法
        '''模拟小狗被命令时坐下'''
        print self.name.title() + " is now sitting!"
    
    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print self.name.title() + " is rolled over!"
``` 

解释一下上面的代码：

* `#1`：这一行是定义类的语法。**类名的首字母大写**。空括号可以理解为每次调用类方法从空白地方生成这个类的实例，
但在`Python2.7`的版本中类方法的定义中括号里要写object，这样用：
`class ClassName(object):`。类名语句下方写**注释简单描述类的功能**。

* `#2`：`__init__`方法，`init`的前后**两个下划线**，这个是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
每当你根据Dog类创建新实例时，Python都会自动运行它。在上面的例子中这个方法有三个形参：`self,name,age`。
在这个方法中，`self`这个形参必不可少，而且必须位于其它形参的前面。
`self`是什么意思呢？书中的解释是：它是一个指向**实例本身**的引用，让实例能够访问类中的**属性和方法**。有点模糊不是么？
现在只是简单地解释一下，这个`self`就等于每次创建的实例。在下一节的[创建实例的地方](#根据类创建实例)做详细的个人理解。
我们将通过实参向`Dog()`传递名字和年龄；`self`会自动传递，因此我们不需要传递它。
每当我们根据类创建实例时，都只需给最后两个形参`(name和age)`提供值。

* `#3`：现在来说说前缀`self`，定义的两个变量都有前缀`self`。
以`self`为前缀的变量都可供类中的所有方法使用(通过点语法，下一节创建实例中会讲到)，我们还可以通过类的任何实例来访问这些变量。
如`self.name = name`获取存储在形参中的值，并将其存储到变量`name`中，然后**该变量被关联到当前创建的实例**，继而变成了每个具体实例的变量。
`self.age = age`的作用与此类似。像这样可**通过实例访问的变量称为属性**。

* `#4`：Dog类还定义了另外两个方法: `sit()`和`roll_over()`。
由于这些方法不需要额外的信息，如名字或年龄，因此它们只有一个形参`self`。我们后面**将创建的实例**能够访问这些方法，换句话说，它们都会蹲下和打滚。
例子中，`sit()`和`roll_over()`所做的有限，它们只是打印一条消息，指出小狗正蹲下或打滚。
但可以扩展这些方法以模拟实际情况:
如果这个类包含在一个计算机游戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码。
如果这个类是用于控制机器狗的，这些方法将引导机器狗做出蹲下和打滚的动作。


<a  id = "根据类创建实例"></a>
#### 根据类创建实例

可将类视为有关如何创建实例的说明。上一节的类是一系列说明，让Python知道如何创建表示特定小狗的实例。 下面来创建一个表示特定小狗的实例:
```
my_dog = Dog("haha",3)
```

来接着上节解释，我们用`Dog`类创建了一个实例：`my_dog`，这个`my_dog`的实例在创建的时候自动调用`__init__`方法，
把方法中的`self`指向创建的实例`my_dog`，让创建的实例`my_dog`可以用**点**语法**访问属性**和**调用方法**。

也就是说我们用类方法创建任何一个实例的时候，都会把这个实例指向类方法里的`self`，
让这个实例可以用**名称访问**我们创建实例时给每个实例赋予的**属性**，还有**调用**这个类里定义的所有**方法**。


<a id = "访问属性"></a>
#### 访问属性

用类方法创建实例之后我们就可以用**实例的名称**加**点语法**来访问创建实例时赋予它的属性了，我们上面已经赋予了`my_dog`名称和年龄的属性，
下面就是访问的例子。
```
print "My dog's name is " + my_dog.name.title() + "!"
print "My dog's age is " + str(my_dog.age) + " years old!"
```

在控制台输出的结果是：
```
My dog's name is Haha!
My dog's age is 3 years old!
```

引用`name`属性的时候，Python先找到实例`my_dog`，再查找与这个实例相关联的属性`name`。
在`Dog`类中引用这个属性时，使用的都是`__init__`方法中的`self.name`，`age`属性类似，因为`self`会自动关联**实例**。

`title()`让首字母大写，`str（）`把数值转化为字符串类型。


<a id = "调用方法"></a>
#### 调用方法

根据`Dog`类创建实例后，就可以使用句点表示法来调用`Dog`类中定义的任何方法。下面来让小狗蹲下和打滚:
```
my_dog.sit()
my_dog.roll_over()
```
前提是`my_dog`这个实例被创建。在控制台输出结果是：
```
Haha is now sitting!
Haha is rolled over!
```
要调用方法，可指定实例的**名称**(这里是`my_dog`)和要调用的方法，并用句点分隔它们。
遇到代码`my_dog.sit()`时，Python在类`Dog`中查找方法`sit()`并运行其代码。 Python以同样的方式解读代码`my_dog.roll_over()`。

还记得上面我们写的方法里也有形参`self`，这个也是会关联实例，让每一个创建的实例可以用**名称加点语法**访问到类中定义的方法。

这种语法很有用。如果给属性和方法指定了**合适的描述性名称**，如`name,age,sit(),roll_over()`，
即便是从未见过的代码块，我们也能够轻松地推断出它是做什么的。


<a id = "创建多个实例"></a>
#### 创建多个实例

可按需求根据类创建任意数量的实例。
```
my_dog = Dog("haha",3)
print "My dog's name is " + my_dog.name.title() + "!"
print "My dog's age is " + str(my_dog.age) + " years old!"
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("lala","4")
print "Your dog's name is " + your_dog.name.title() + "!"
print "Your dog's age is " + str(your_dog.age) + " years old!"
your_dog.sit()
your_dog.roll_over()
```
在上面例子中，我们创建了两条小狗，它们分别名为haha和lala。每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作:
```
My dog's name is Haha!
My dog's age is 3 years old!
Haha is now sitting!
Haha is rolled over!
Your dog's name is Lala!
Your dog's age is 4 years old!
Lala is now sitting!
Lala is rolled over!
```

就算我们给第二条小狗指定同样的名字和年龄，Python依然会根据Dog类创建另一个实例。

你可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在**不同的变量**中，或占用**列表或字典**的不同位置。


<a id ="使用类和实例"></a>
### 使用类和实例

你可以使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间都将花在使用根据类创建的实例上。

你需要执行的一个重要任务是修改实例的属性。你可以**直接修改**实例的属性，也可以**编写方法以特定的方式进行修改**。


<a id = "car类"></a>
#### car类

下面来编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法:
```
class Car():
    '''模拟汽车的尝试'''
    def __init__(self,make,model,year):
        '''初始化汽车实例的属性'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car("audi","a4",2018)   # 创建 my_new_car 这个实例
print my_new_car.get_descriptive_name() # 调用 描述方法
```

控制台会输出：
```
2018 Audi A4
```


<a id = "给属性指定默认值"></a>
#### 给属性指定默认值

类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法`__init__()`内指定这种初始值是可行的;
如果你对某个属性这样做了，就**无需包含**为它提供初始值的**形参**。

下面来添加一个名为`odometer_reading`的属性，其初始值总是为0。我们还添加了一个名为`read_odometer()`的方法，用于读取汽车的里程表:
```
 def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print "This car has " + str(self.odometer_reading) + " miles on it."

my_new_car.read_odometer() #调用 查看汽车里程的方法
```
在控制台输出为：
```
This car has 0 miles on it.
```


<a id = "修改属性的值"></a>
#### 修改属性的值

因为里程这个属性不可能不变，所以我们要有途径去修改它。

可以以**三种不同的方式**修改属性的值。


<a id = "直接通过实例进行修改"></a>
##### 1、直接通过实例进行修改

要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为27:
```
my_new_car.read_odometer() #调用 查看汽车里程的方法
my_new_car.odometer_reading = 27 #直接通过实例修改属性
my_new_car.read_odometer()
```

输出为：
```
This car has 0 miles on it.
This car has 27 miles on it.
```

简单解释一下：我们使用句点表示法来直接访问并设置汽车的属性`odometer_reading`。
这行代码让Python在实例`my_new_car`中找到属性`odometer_reading`，并将该属性的值设置为27。

我们从输出的结果可以看到，没修改前是默认值0，修改后变成27，说明修改成功了。


<a id = "通过方法进行设置"></a>
##### 2、通过方法进行设置

如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
下面的示例演示了一个名为`update_odometer()`的方法:
```
def update_odometer(self,mileage):
        '''将里程表的值设定为指定值'''
        self.odometer_reading = mileage
```

我们使用一下：
```
my_new_car.read_odometer() #调用 查看汽车里程的方法
my_new_car.update_odometer(27) #使用方法修改里程数
my_new_car.read_odometer()
```

输出的结果为：
```
This car has 0 miles on it.
This car has 27 miles on it.
```

简单解释一下：

方法接受一个里程值，并将其存储到`self.odometer_reading`中，例子中我们调用的时候提供了27，故而将里程的值设置为27，
输出的结果也显示我们设置成功了。

可对方法`update_odometer`进行扩展，使其在修改里程表读数时做些额外的工作。

下面来修改一下上面的方法，添加一些逻辑，禁止任何人将里程表读数往回调:
```
 def update_odometer(self,mileage):
        '''将里程表的值设定为指定值
           禁止将里程表的读数往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print "You can't roll back an odometer!"
```

现在，`update_odometer()`在修改属性前检查指定的读数是否合理。如果新指定的里程(`mileage`)大于或等于原来的里程(`self.odometer_reading`)，
就将里程表读数改为新指定的里程;否则就发出警告，指出不能将里程表往回拨。


<a id = "通过方法进行递增"></a>
##### 3、通过方法进行递增（增加特定的值）

有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程。

下面的方法让我们能够传递这个增量，并相应地增加里程表读数:
```
def increment_odometer(self,miles):
        '''将里程表读数增加指定的量
           禁止增加负值把里程数回调 
        '''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print "You can't roll back an odometer!"
```
测试一下：
```
my_new_car = Car("audi","a4",2018)   # 创建 my_new_car 这个实例
print my_new_car.get_descriptive_name() # 调用 描述性方法
my_new_car.read_odometer() #调用 查看汽车里程的方法

my_new_car.update_odometer(23500) #更新my_new_car这个实例的里程数
my_new_car.read_odometer() #现在是23500

my_new_car.increment_odometer(100) #my_new_car这个实例增加100公里的里程
my_new_car.read_odometer() #现在是23600

```
输出的结果为：
```
2018 Audi A4
This car has 0 miles on it.
This car has 23500 miles on it.
This car has 23600 miles on it.
```


<a id = "继承"></a>
### 继承

编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法;原有的类称为父类，而新类称为子类。
子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。


<a id = "子类的方法"></a>
#### 子类的方法`__init__()`

创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法`__init__()`需要父类施以援手。

例如，下面来模拟电动汽车。
电动汽车是一种特殊的汽车，因此我们可以在前面创建的Car类的基础上创建新类ElectricCar，这样我们就只需为电动汽车特有的属性和行为编写代码。

下面来创建一个简单的ElectricCar类版本，它具备Car类的所有功能:
```
class ElectricCar(Car):  #必须在括号里指定父类的名称
    '''电动汽车类的定义'''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
```

解释一下这个类声明：

`super()`是一个特殊函数，帮助Python将**父类和子类关联**起来。这行代码让Python调用`ElectricCar`的父类的方法`__init__()`，
让实例`ElectricCar`包含父类的所有属性。父类也称为**超类 (superclass)**，名称super因此而得名。

测试使用一下：
```
my_electric_car = ElectricCar("tesla","model s","2017")
print (my_electric_car.get_descriptive_name())
print (my_electric_car.odometer_reading)
```
解释一下测试：

为测试继承是否能够正确地发挥作用，我们尝试创建一辆电动汽车，但提供的信息与创建普通汽车时相同。

在第一行，我们创建ElectricCar类的一个实例，并将其存储在变量`my_electric_car`中。
这行代码调用类中定义的方法`__init__`，后者让Python调用父类Car中定义的方法`__init__`。我们提供了实参`tesla`、`model s`和`2017`。

因为调用的是父类的`__init__`方法，所以子类ElectricCar创建的实例里也会有一个初始化的属性`odometer_reading`，当然也是为0的。

在控制台输出如下：
```
2017 Tesla Model S
0
```


<a id = "给子类定义属性和方法"></a>
#### 给子类定义属性和方法

除方法`__init__`外，电动汽车没有其他特有的属性和方法。当前，我们只想确认电动汽车具备普通汽车的行为，也就是父类里已经定义的方法。

当前，ElectricCar实例的行为与Car实例一样，但现在我们可以开始定义电动汽车特有的属性和方法了。

让一个类继承另一个类后，可添加**区分子类和父类**所需的**新**属性和方法。

下面来改一下刚才的代码，添加一个电动汽车特有的属性(电瓶)，以及一个描述该属性的方法。
我们将存储电瓶容量，并编写一个打印电瓶描述的方法:
```
class ElectricCar(Car): #必须在括号里指定父类的名称
    '''电动汽车类的定义
       先初始化父类的属性，再初始化电动车特有的属性。
    '''
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery_size = 70  #电动车特有属性,Car的实例就不具有这个属性
    
    def describe_battery(self):
        '''打印一条描述电瓶容量的信息'''
        print ("This car has a " + str(self.battery_size) + "-kwh battery!")
```
我们再试试属性和方法：
```
my_electric_car = ElectricCar("tesla","model s","2017")
print (my_electric_car.battery_size)
my_electric_car.describe_battery()
```
输出为：
```
70
This car has a 70-kwh battery!
```
我们可以清晰地知道，我们子类创建的实例已经具有了它特有的属性和方法。

对于例子的子类ElectricCar类的特殊化程度没有任何限制。模拟电动汽车时，你可以根据所需的准确程度添加**任意数量的属性和方法**。

如果一个属性或方法是任何汽车都有的，而不是电动汽车特有的，就应将其加入到父类Car类而不是子类ElectricCar类中。
这样，使用Car类的人将获得相应的功能，而ElectricCar类只包含处理电动汽车**特有属性和行为的代码。**


<a id = "重写父类的方法"></a>
#### 重写父类的方法

对于父类的方法，只要它**不符合子类模拟的实物的行为**，都可对其进行重写。为此，可在子类中定义一个这样的方法，即**它与要重写的父类方法同名**。
这样，Python将不会考虑这个父类方法，而只**关注你在子类中定义的相应方法，因为它会从本身先找（自下而上）**。

假设我们在Car中定义一个邮箱的方法：
```
def fill_gas_tank(self):
        '''描述油箱信息'''
        print ("This car has a gas tank!")
```

那么我们的子类里也会继承这个方法，但是显而易见电动车没有油箱，也并不需要，这时候我们就要在ElectricCar类中重写这个方法：
```
def fill_gas_tank(self):
        '''重写油箱的方法'''
        print ("This car doesn't need a gas tank!")
```
如果有人对电动汽车调用`fill_gas_tank()`方法，Python将忽略Car类中的方法`fill_gas_tank()`，转而运行子类ElectricCar中重写的方法。
使用继承时，可让子类保留从父类那里继承而来的精华，并剔除不需要的糟粕。


<a id = "将实例用作属性"></a>
#### 将实例用作属性






