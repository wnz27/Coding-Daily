# Dive into Python3      |         《深入python3》

首先这本书是免费的并且作者授权了可以进行任何自由使用，[授权声明](https://creativecommons.org/licenses/by-sa/3.0/deed.zh)

然后英文的原版链接在这，[Dive into Python3](http://diveinto.org/python3/index.html)

## -1、这本书有哪些新特性
先略，先把主要内容搞定

## 0、安装python
这章我就略过了，主要内容如果我不幸翻译完也一样不啰嗦了~~~~~~

## 1、你的第一个Python程序
### 1.1深入进去
传统的叙述就是我应该跟你念叨一些基础的编程的代码块，让我们可以逐步的构建一些有用的东西。让我们跳过这些，这是一个完整的可以运行的pyhton程序。
它也许会让你不能完全理解。不用担心，因为你将要逐行的分析它，如果可以的话，看看你能做些什么！
【文件名：humansize.py】
```
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
```

现在让我们在命令行执行这个程序。在windows，它应该看起来是这样的：
```
c:\home\diveintopython3\examples> c:\python31\python.exe humansize.py
1.0 TB
931.3 GiB
```
在Mac OS X 或者 Linux下执行，应该看起来是这样的：
```
you@localhost:~/diveintopython3/examples$ python3 humansize.py
1.0 TB
931.3 GiB
```

发生了什么呢？你执行了你第一个python程序，你在命令行调用了pyhton的解释器，然后你给pyhton传递了你希望它执行的脚本的名字。
这个脚本定义了一个单一的函数，`approximate_size()`,这个函数接收一个以比特（字节）为单位的确切的文件大小，计算出一个“漂亮”（但大约）的大小。
（你可能在windows的资源管理器，或者Mac OS X访达，或者Ubuntu里的Nautilus或者海豚或者运行于linux和类unix平台的Thunar文件管理器，如果你用多行
列表的形式去展示文件夹的文件，他会用一个表来显示文件图标，文件名称，大小，类型，最后修改时间等等。如果文件夹包含一个1093字节的名为TODO的文件，那么
你的文件管理器不会显示TODO 1093bytes，而是会显示TODO 1KB，这就是`approximate_size()`函数所做的事情）
看看这个脚本的最下面，你将会看到打印两次调用这个函数。这些就是函数调用，一次调用传递一些参数，然后把函数返回值直接传递给`print()`函数。
`print()`函数是python内置的；你绝对不会看到任何一个对它的明确的声明。你就是可以使用它，任何时间，任何地点，只要小爷喜欢。
（这有非常多的内置函数，还有更多函数分开在不同的模块。Patiencce， grasshopper）
所以为什么每次在命令行运行这个脚本都会给你相同的输出？我们会做到这点。首先让我们看看`approximate_size()`这个函数

### 1.2函数声明
侧边贴士：当你需要一个函数，声明它就可以了。


Python has functions like most other languages, but it does not have separate header files like c++ or interface/implementation sections like Pascal. When you need a function, just declare it, like this:

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
The keyword def starts the function declaration, followed by the function name, followed by the arguments in parentheses. Multiple arguments are separated with commas.
Also note that the function doesn’t define a return datatype. Python functions do not specify the datatype of their return value; they don’t even specify whether or not they return a value. (In fact, every Python function returns a value; if the function ever executes a return statement, it will return that value, otherwise it will return None, the Python null value.)
> In some languages, functions (that return a value) start with function, and subroutines (that do not return a value) start with sub. There are no subroutines in Python. Everything is a function, all functions return a value (even if it’s None), and all functions start with def.
The approximate_size() function takes the two arguments — size and a_kilobyte_is_1024_bytes — but neither argument specifies a datatype. In Python, variables are never explicitly typed. Python figures out what type a variable is and keeps track of it internally.
> In Java and other statically-typed languages, you must specify the datatype of the function return value and each function argument. In Python, you never explicitly specify the datatype of anything. Based on what value you assign, Python keeps track of the datatype internally.