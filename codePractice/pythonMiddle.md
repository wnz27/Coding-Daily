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
** *如果导入的模块不存在，Python解释器会报 ImportError 错误* **：
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








