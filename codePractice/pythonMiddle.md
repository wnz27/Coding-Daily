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

