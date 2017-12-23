# Python middle
## 如果遇到名字冲突怎么办？比如math模块有一个log函数，logging模块也有一个log函数，如果同时使用，如何解决名字冲突？
如果使用import导入模块名，由于必须通过模块名引用函数名，因此不存在冲突：
```
import math, logging
print math.log(10)   # 调用的是math的log函数
logging.log(10, 'something')   # 调用的是logging的log函数
```
如果使用 from...import 导入 log 函数，势必引起冲突。这时，可以给函数起个“别名”来避免冲突：
```
from math import log
from logging import log as logger   # logging的log现在变成了logger
print log(10)   # 调用的是math的log
logger(10, 'import from logging')   # 调用的是logging的log
```
* 任务
Python的os.path模块提供了 isdir() 和 isfile()函数，请导入该模块，并调用函数判断指定的目录和文件是否存在。
注意: 
1. 由于运行环境是平台服务器，所以测试的也是服务器中的文件夹和文件，该服务器上有/data/webroot/resource/python文件夹和/data/webroot/resource/python/test.txt文件，大家可以测试下。
2. 当然，大家可以在本机上测试是否存在相应的文件夹和文件。
```
import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')
```
**hint:**
注意到os.path模块可以以若干种方式导入：
```
import os
import os.path
from os import path
from os.path import isdir, isfile
```
每一种方式调用 isdir 和 isfile 都有所不同。
```
参考代码:
import os
print os.path.isdir(r'/data/webroot/resource/python')
print os.path.isfile(r'/data/webroot/resource/python/test.txt')
```
**result：**
```
from os.path import isdir,isfile
print isdir(r'/data/webroot/resource/python')
print isfile(r'/data/webroot/resource/python/test.txt')

from os.path import isdir,isfile
print isdir(r'/data/webroot/conf')
print isfile(r'/data/webroot/conf/app.conf')
```

## python中动态导入模块
***如果导入的模块不存在，Python解释器会报 ImportError 错误***：
```
>>> import something
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named something
```
有的时候，两个不同的模块提供了相同的功能，比如 StringIO 和 cStringIO 都提供了StringIO这个功能。这是因为Python是动态语言，解释执行，因此Python代码运行速度慢。
如果要提高Python代码的运行速度，最简单的方法是把某些关键函数用 C 语言重写，这样就能大大提高执行速度。
同样的功能，**StringIO 是纯Python代码编写的，而 cStringIO 部分函数是 C 写的，因此 cStringIO 运行速度更快。**
利用ImportError错误，我们经常在Python中动态导入模块：
```
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
```
上述代码先尝试从cStringIO导入，如果失败了（比如cStringIO没有被安装），再尝试从StringIO导入。这样，如果cStringIO模块存在，则我们将获得更快的运行速度，如果cStringIO不存在，则顶多代码运行速度会变慢，但不会影响代码的正常执行。
try 的作用是捕获错误，并在捕获到指定错误时执行 except 语句。
```
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python':2.7})
```


## python之使用__future__
Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。要“试用”某一新的特性，就可以通过导入__future__模块的某些功能来实现。
例如，Python 2.7的整数除法运算结果仍是整数：
```
>>> 10 / 3
3
```
但是，Python 3.x已经改进了整数的除法运算，“/”除将得到浮点数，“//”除才仍是整数：
```
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
```
要在Python 2.7中引入3.x的除法规则，导入__future__的division：
```
>>> from __future__ import division
>>> print 10 / 3
3.3333333333333335
```
当新版本的一个特性与旧版本不兼容时，该特性将会在旧版本中添加到__future__中，以便旧的代码能在旧版本中测试新特性。
* 任务
在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b。请利用__future__的unicode_literals在Python 2.7中编写unicode字符串。
```
from __future__ import unicode_literals 
s = 'am I an unicode?'
print isinstance(s, unicode)
```


## python之定义类并创建实例
在Python中，类通过 class 关键字定义。以 Person 为例，定义一个Person类如下：
```
class Person(object):
    pass
```
按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，现在我们只需要简单地从object类继承。
有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。创建实例使用 类名+()，类似函数调用的形式创建：
```
xiaoming = Person()
xiaohong = Person()
```
* 任务
请练习定义Person类，并创建出两个实例，打印实例，再比较两个实例是否相等。
```
class Person(object):
    pass
xiaoming = Person()
xiaohong = Person()
print xiaoming
print xiaohong
print xiaoming == xiaohong
```

## python中创建实例属性
虽然可以通过Person类创建出xiaoming、xiaohong等实例，但是这些实例看上除了地址不同外，没有什么其他不同。在现实世界中，区分xiaoming、xiaohong要依靠他们各自的名字、性别、生日等属性。
如何让每个实例拥有各自不同的属性？由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：
```
xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'
```
给xiaohong加上的属性不一定要和xiaoming相同：
```
xiaohong = Person()
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2
```
实例的属性可以像普通变量一样进行操作：
`xiaohong.grade = xiaohong.grade + 1`
* 任务
请创建包含两个 Person 类的实例的 list，并给两个实例的 name 赋值，然后按照 name 进行排序。
```
class Person(object):
    pass
p1 = Person()
p1.name = 'Bart'
p2 = Person()
p2.name = 'Adam'
p3 = Person()
p3.name = 'Lisa'
L1 = [p1, p2, p3]
L2 = sorted(L1,lambda p1,p2:cmp(p1.name,p2.name))
print L2[0].name
print L2[1].name
print L2[2].name
```

## python中初始化实例属性
虽然我们可以自由地给一个实例绑定各种属性，但是，现实世界中，一种类型的实例应该拥有相同名字的属性。例如，Person类应该在创建的时候就拥有 name、gender 和 birth 属性，怎么办？
在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
```
class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
```
__init__() 方法的第一个参数必须是 self（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别。
相应地，创建实例时，就必须要提供除 self 以外的参数：
```
xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
```
有了__init__()方法，每个Person实例在创建时，都会有 name、gender 和 birth 这3个属性，并且，被赋予不同的属性值，访问属性使用.操作符：
```
print xiaoming.name
# 输出 'Xiao Ming'
print xiaohong.birth
# 输出 '1992-2-2'
```
要特别注意的是，初学者定义__init__()方法常常忘记了 self 参数：
```
>>> class Person(object):
...     def __init__(name, gender, birth):
...         pass
... 
>>> xiaoming = Person('Xiao Ming', 'Male', '1990-1-1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 3 arguments (4 given)
```
这会导致创建失败或运行不正常，因为第一个参数name被Python解释器传入了实例的引用，从而导致整个方法的调用参数位置全部没有对上。
* 任务
请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
```
class Person(object):
    def __init__(self,name,gender,birth,job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print xiaoming.name
print xiaoming.job
```

## python中访问限制
我们可以给一个实例绑定很多属性，如果有些属性不希望被外部访问到怎么办？
Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问。看例子：
```
class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob')
print p.name
# => Bob
print p._title
# => Mr
print p.__job
# => Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__job'
```
可见，只有以双下划线开头的"__job"不能直接被外部访问。
但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。
以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。
* 任务
请给Person类的__init__方法中添加name和score参数，并把score绑定到__score属性上，看看外部是否能访问到。
```
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
p = Person('Bob', 59)
print p.name
print p.__score
```
display:
```
Traceback (most recent call last):
  File "index.py", line 9, in 
    print p.__score
AttributeError: 'Person' object has no attribute '__score'
```

## python中创建类属性
类是模板，而实例则是根据类创建的对象。
绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。
定义类属性可以直接在 class 中定义：
```
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
```
因为类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：
```
print Person.address
# => Earth
```
对一个实例调用类的属性也是可以访问的，所有实例都可以访问到它所属的类的属性：
```
p1 = Person('Bob')
p2 = Person('Alice')
print p1.address
# => Earth
print p2.address
# => Earth
```
由于Python是动态语言，类属性也是可以动态添加和修改的：
```
Person.address = 'China'
print p1.address
# => 'China'
print p2.address
# => 'China'
```
因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了。
任务
请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
```
class Person(object):
    count = 0
    def __init__(self,name):
        Person.count = Person.count + 1
        self.name = name

p1 = Person('Bob')
print Person.count
p2 = Person('Alice')
print Person.count
p3 = Person('Tim')
print Person.count
```


## python中类属性和实例属性名字冲突怎么办
修改类属性会导致所有实例访问到的类属性全部都受影响，但是，如果在实例变量上修改类属性会发生什么问题呢？
```
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')
print 'Person.address = ' + Person.address
p1.address = 'China'
print 'p1.address = ' + p1.address
print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address
```
结果如下：
```
Person.address = Earth
p1.address = China
Person.address = Earth
p2.address = Earth
```
我们发现，在设置了 p1.address = 'China' 后，p1访问 address 确实变成了 'China'，但是，Person.address和p2.address仍然是'Earch'，怎么回事？
原因是 p1.address = 'China'并没有改变 Person 的 address，而是给 p1这个实例绑定了实例属性address ，对p1来说，它有一个实例属性address（值是'China'），而它所属的类Person也有一个类属性address，所以:
访问 p1.address 时，优先查找实例属性，返回'China'。
访问 p2.address 时，p2没有实例属性address，但是有类属性address，因此返回'Earth'。
可见，当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。
当我们把 p1 的 address 实例属性删除后，访问 p1.address 就又返回类属性的值 'Earth'了：
```
del p1.address
print p1.address
# => Earth
```
可见，千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。
* 任务
请把上节的 Person 类属性 count 改为 __count，再试试能否从实例和类访问该属性。
```
class Person(object):
    __count = 0
    def __init__(self, name):
        Person.__count = Person.__count + 1
        self.name = name
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')
print Person.__count
```
display:
```运行失败
Traceback (most recent call last):
  File "index.py", line 13, in 
    print Person.__count
AttributeError: type object 'Person' has no attribute '__count'
1
2
```


## python中定义实例方法
一个实例的私有属性就是以__开头的属性，无法被外部访问，那这些属性定义有什么用？
虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。除了可以定义实例的属性外，还可以定义实例的方法。
实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：
```
class Person(object):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
```
get_name(self) 就是一个实例方法，它的第一个参数是self。__init__(self, name)其实也可看做是一个特殊的实例方法。
调用实例方法必须在实例上调用：
```
p1 = Person('Bob')
print p1.get_name()  # self不需要显式传入
# => Bob
```
在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。
* 任务
请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，能根据 __score 的值分别返回 A-优秀, B-及格, C-不及格三档。
```
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_grade(self):
        if self.__score >= 85 and self.__score <= 100:
            return "A"
        elif self.__score >= 60 and self.__score <85:
            return "B"
        else:
            return "C"
p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)
print p1.get_grade()
print p2.get_grade()
print p3.get_grade()
```


## python中方法也是属性
我们在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象：
```
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob', 90)
print p1.get_grade
# => <bound method Person.get_grade of <__main__.Person object at 0x109e58510>>
print p1.get_grade()
# => A
```
也就是说，p1.get_grade 返回的是一个函数对象，但这个函数是一个绑定到实例的函数，p1.get_grade() 才是方法调用。
因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType() 把一个函数变为一个方法：
```
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
print p2.get_grade()
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade
```
给一个实例动态添加方法并不常见，直接在class中定义要更直观。
* 任务
由于属性可以是普通的值对象，如 str，int 等，也可以是方法，还可以是函数，大家看看下面代码的运行结果，请想一想 p1.get_grade 为什么是函数而不是方法：
```
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()
```
* **直接把 lambda 函数赋值给 self.get_grade 和绑定方法有所不同，函数调用不需要传入 self，但是方法调用需要传入 self。**











