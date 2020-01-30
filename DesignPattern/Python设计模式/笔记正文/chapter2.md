## 第二章 单例设计模式
单例设计模式是应用开发过程中最简单和最著名的一种创建型设计模式。
本章还会介绍Monostate（或者Borg）设计模式，它是单例设计模式的一个变种。
本章涉及主题：
* 理解单例设计模式
* 单例模式实例
* 单例设计模式的Python实现
* Monostate（Borg）模式
### 2.1 理解单例设计模式
单例模式提供了这样一个机制，即确保类有且只有一个特定类型的对象，并提供全局访问点。
因此，单例模式通常用于下列情形，例如日志记录或数据库操作、打印机后台处理程序，
以及其他程序---该程序运行过程中只能生成一个实例，以避免对同一资源产生相互冲突的请求。
例如，我们可能希望使用一个数据库对象对数据库进行操作，以维护数据的一致性；
或者希望一个日志类的对象，将多项服务的日志信息按照顺序转储存到一个特定的日志文件中。
简言之，单例模式特点如下：
* 确保类有且只有一个对象被创建。
* 为对象提供一个访问点，以使用程序可以全局访问该对象。
* 控制共享资源的并行访问。

实现单例模式的一个简单地方法是，使构造函数私有化，并创建一个静态方法来完成对象的初始化。
这样，对象在第一次调用时创建，此后这个类将返回同一个对象。
在使用Python的时候，我们实现方式要有所变通，因为它无法创建私有的构造函数。
#### 利用Python实现经典的单例模式
下面是基于Python的单例模式实现代码，它主要完成了两件事情。
1. 只允许Singleton类生成一个实例。
2. 如果已经有了一个实例了，我们会重复提供同一个对象。
具体代码如下:
```
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

s = Singleton()
print('Object created', s)

s1 = Singleton()
print('Object created', s1)
```
输出
```
Object created <__main__.Singleton object at 0x107b051f0>
Object created <__main__.Singleton object at 0x107b051f0>
<__main__.Singleton object at 0x10a1af1f0>
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.1.py)

在上面的代码中，我们通过覆盖`__new__`方法（Python用于实例化对象的特殊方法）
来控制对象的创建。对象s就是由`__new__`方法创建的，但在创建之前，
该方法会检查对象是否已存在。
方法hasattr（Python的特殊方法，用来了解对象是否具有某个属性）
用于查看对象cls是否具有属性instance，该属性的作用是检查该类是否已经生成了一个对象。
当对象s1被请求的时候，hasattr()发现对象已经存在，
所以，对象s1将被分配已有的对象实例（地址位于0x10a1af1f0）
### 2.2 单例模式中的懒汉式实例化
单例模式的用例之一就是懒汉式实例化。例如，再导入模块的时候我们可能会无意中创建一个对象，
但当时根本用不到它。懒汉式实例化能够确保在实际需要时才创建对象。
所以，懒汉式实例化是一种节约资源并仅在需要时才创建它们的方式。

在下面的代码示例中，执行`s = Singleton()`的时候，它会调用`__init__`方法，
但没有新的对象被创建。然而，实际的对象创建发生在调用`Singleton.getInstance()`
的时候，我们正是通过这种方式来实现懒汉式实例化的。

```
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    
s = Singleton()  ## class initialized, but object not created
print('*' * 80)
print("Object created", Singleton.getInstance())  # Object gets created here
print('*' * 80)
s1 = Singleton()  ## instance already created
```
输出：
```
 __init__method called..
********************************************************************************
 __init__method called..
Object created <__main__.Singleton object at 0x106330250>
********************************************************************************
Instance already created: <__main__.Singleton object at 0x106330250>
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.2.py)

### 2.3 模块级别的单例模式
默认情况下，所有模块都是单例，这是由Python的导入行为所决定的。
Python通过下列方式来工作。
1. 检查一个Python模块是否已经导入。
2. 如果已经导入，则返回该模块的对象。
如果还没有导入，则导入该模块，并实例化。
3. 因此，当模块被导入的时候，它就会被实例化。然而，当同一个模块被再次导入的时候，
它不会再次初始化，因为单例模式只能有一个对象，所以，它会返回同一个对象。
### 2.4 Monostate单例模式
GoF的单例设计模式是指，一个类有且只有一个对象。
根据Alex Martelli的说法，通常程序员需要的是让实例共享相同的状态。
他建议开发人员应该关注状态和行为，而不是同一性。
由于该概念基于所有对象共享相同状态，因此它也被称为Monostate（单态）模式。
Monostate模式可以通过Python轻松实现。在下面的代码中，我们将类变量
`__shared_state`赋给变量`__dict__`（它是Python的一个特殊变量）。
Python使用`__dict__`存储一个类所有对象的状态。在下面的代码中，
我们故意把`__shared_state`赋给所有已经创建的实例。
所以，如果我们创建了两个实例“b”和“b1”，我们将得到两个不同的对象，
这一点与单例模式大为不同，后者只能生成一个对象。
然而对象的状态即`b.__dict__`和`b1.__dict__`却是相同的。
现在，就算对象b的对象变量x发生了变化，这个变化也会复制到被所有对象共享
的`__dict__`变量，即b1的变量x的值也会从1变为4。
```
class Borg:
    __shared_state = {"1" : "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4
print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
print("Borg Object 'b1': ", b1)
print("Object State 'b': ", b.__dict__)  ## b and b1 share same state
print("Object State 'b1': ", b1.__dict__)
```
输出
```
Borg Object 'b':  <__main__.Borg object at 0x1097ff6a0>
Borg Object 'b1':  <__main__.Borg object at 0x1097f8940>
Object State 'b':  {'1': '2', 'x': 4}
Object State 'b1':  {'1': '2', 'x': 4}
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.4.1.py)

除此以外，我们还可以通过修改`__new__`方法本身来实现Borg模式。
我们知道，`__new__`方法是用来创建对象的实例的，具体如下所示：
```
class Borg(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
b = Borg()
b1 = Borg()
b.x = 4
print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
print("Borg Object 'b1': ", b1)
print("Object State 'b': ", b.__dict__)  ## b and b1 share same state
print("Object State 'b1': ", b1.__dict__)
```
输出：
```
Borg Object 'b':  <__main__.Borg object at 0x1017021f0>
Borg Object 'b1':  <__main__.Borg object at 0x101702220>
Object State 'b':  {'x': 4}
Object State 'b1':  {'x': 4}
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.4.2.py)

### 2.5 单例和元类
元类是一个类的类，这意味着该类是它的元类的实例。使用元类，
程序员有机会从预定义的Python类创建自己类型的类。例如，你有一个
对象MyClass，你可以创建一个元类MyKls,它按照你需要的方式重新定义
MyClass的行为。下面，来深入介绍它们。
在Python中，一切皆对象。如果我们说`a=5`，则`type(a)`返回
`<type'int'>`，这意味着a是int类型。
但是，`type(int)`返回`<type'type'>`，这表明存在一个元类，
因为int是type类型的类。
类的定义由它的元类决定，所以当我们用类A创建一个类时，Python
通过`A=type(name, bases, dict)`创建它。
* name: 这是类的名称
* bases: 这是基类
* dict: 这是属性变量

现在，如果一个类有一个预定义的元类（名为Metals），那么Python就会通过
`A=Metals(name, bases, dict)`来创建这个类。
让我们看看一个示例元类的实现：
```
class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwds)
    
class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(2, 7)
```
输出：
```
***** Here's My int ***** (2, 7)
Now do whatever you want with these objects...
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.5.1.py)

对于已经存在的类来说，当需要创建对象时，将调用Python的特殊方法`__call__`。
在这段代码中，当我们使用int(2,7)实例化int类时，MyInt元类的`__call__`方法
将被调用，这意味着现在元类控制着对象的实例化。

前面的思路同样适用于单例设计模式。由于元类对类创建和对象实例化有更多的控制权，
所以它可以用于创建单例。（注意：为了控制类的创建和初始化，
元类将覆盖`__new__`和`__init__`方法。）

以下示例代码能够更好地帮我们解释基于元类的单例实现：
```
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, ** kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print(super(),cls,'+',cls._instances)
        return cls._instances[cls]
    
class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
```
输出：
```
<super: <class 'MetaSingleton'>, <MetaSingleton object>> <class '__main__.Logger'> + {<class '__main__.Logger'>: <__main__.Logger object at 0x108590250>}
<__main__.Logger object at 0x108590250> <__main__.Logger object at 0x108590250>
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.5.2.py)

### 2.6 单例模式一
作为一个实际的用例，我们将通过一个数据库应用程序来展示单例的应用。
这里不妨以需要对数据库进行多种读取和写入操作的云服务为例进行讲解。
完整的云服务被分解为多个服务，每个服务执行不同的数据库操作。
针对UI（Web应用程序）上的操作将导致调用API,最终产生相应的DB操作。
很明显，跨不同服务的共享资源是数据库本身。
因此如果我们需要更好地设计云服务，必须注意以下几点：
* 数据库中操作的一致性，即一个操作不应与其他操作发生冲突。
* 优化数据库的各种操作，以提高内存和CPU的利用率。
这里提供一个示例Python实现：
```
import sqlite3
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
```
输出：
```
Database Objects DB1 <sqlite3.Cursor object at 0x10e877f80>
Database Objects DB2 <sqlite3.Cursor object at 0x10e877f80>
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.6.py)

通过阅读上面的代码，我们会发现以下几点。
1. 我们以MetaSingleton为名创建了一个元类。就像在上一节中解释的那样，
Python的特殊方法`__call__`可以通过元类创建单例。
2. 数据库类由MetaSingleton类装饰后，其行为就会表现为单例。因此，当
数据库类被实例化时，它只能创建一个对象。
3. 当Web应用程序对数据库执行某些操作时，它会多次实例化数据库类，但只创建一个对象。
因为只有一个对象，所以对数据库的调用是同步。此外，这样还能够节约系统资源，并且可以
避免消耗过多的内存或CPU资源。

假如我们要开发的不是单个Web应用程序，而是集群化的情形，即多个Web应用共享单个数据库。

当然，单例在这种情况下好像不太好使，因为每增加一个Web应用程序，就要新建一个单例，
添加一个新的对象来查询数据库。

这导致数据库操作无法同步，并且要耗费大量的资源。
在这种情况下，数据库的链接池比实现单例要好得多。

### 2.7 单例模式二
让我们考虑另一种情况，即为基础设施提供运行状况监控服务（就像Nagios所做的那样）。

我们创建了HealthCheck类，它作为单例实现。我们还要维护一个被监控的服务器列表。

当一个服务器从这个列表中删除时，监控软件应该觉察到这一情况，并从被监控的服务器
列表中将其删除。

在下面的代码中，hc1和hc2对象与单例中的类相同。
我们可以使用`addServer()`方法将服务器添加到基础设施中，以进行运行状况检查。

首先，通过迭代对这些服务器的运行状况进行检查。之后，`changeServer()`方法

会删除最后一个服务器，并向计划进行运行状况检查的基础设施中添加一个新服务器。

因此，运行状况检查进行第二次迭代时，它会使用修改后的服务器列表。

所有这一切都可以借助单例模式来完成。当添加或删除服务器时，运行状况的检查工作
必须由了解基础设施变动情况的同一个对象来完成：
```
class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super().__new__(cls, *args, **kwargs)
        return HealthCheck._instance
    
    def __init__(self):
        self._servers = []
    
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])
```
输出：
```
Schedule health check for servers (1)..
Checking  Server 1
Checking  Server 2
Checking  Server 3
Checking  Server 4
Schedule health check for servers (2)..
Checking  Server 1
Checking  Server 2
Checking  Server 3
Checking  Server 5
```
[代码版本：Python v3.8.0](../相关代码/第二章/2.7.py)
### 2.8 单例模式的缺点
虽然单例模式在许多情况下效果很好，但是这种模式仍然存在一些缺陷。
由于单例具有全局访问权限，因此可能出现以下问题：
* 全局变量可能在某处已经被误改，但是开发人员仍然认为它们没有发生
变化，而该变量还在应用程序的其他位置被使用。
* 可能会对同一对象创建多个引用。由于单例只创建一个对象，因此这种
情况下会对同一个对象创建多个引用。
* 所有依赖于全局变量的类都会由于一个类的改变而紧密耦合为全局数据，
从而可能在无意中影响另一个类。

### 提示，小结
关于单例模式以下几点需牢记：
* 在许多实际应用程序中，我们只需要创建一个对象，如线程池、缓存、
对话框、注册表设置等。如果我们为每个应用程序创建多个实例，则会
导致资源的过度使用。单例模式在这种情况下工作得很好。
* 单例是一种经过时间考验的成熟方法，能够在不带来太多缺陷的情况
下提供全局访问点。
* 该模式也有一些缺点。当使用全局变量或类实例化非常耗费资源但最终
却没有用到它们的情况下，单例的影响可以忽略不计。