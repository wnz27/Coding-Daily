# Dive into Python3      |         《深入python3》

首先这本书是免费的并且作者授权了可以进行任何自由使用，[授权声明](https://creativecommons.org/licenses/by-sa/3.0/deed.zh)

然后英文的原版链接在这，[Dive into Python3](http://diveinto.org/python3/index.html)

## -1、这本书有哪些新特性
先略，先把主要内容搞定

## 0、安装python
这章我就略过了，主要内容如果我不幸翻译完也一样不啰嗦了~~~~~~

## 1、你的第一个Python程序
### 1.深入进去
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
（你可能在windows的资源管理器，或者Mac OS X）

(You’ve probably seen this in Windows Explorer, or the Mac OS X Finder, or Nautilus or Dolphin or Thunar on Linux. If you display a folder of documents as a multi-column list, it will display a table with the document icon, the document name, the size, type, last-modified date, and so on. If the folder contains a 1093-byte file named TODO, your file manager won’t display TODO 1093 bytes; it’ll say something like TODO 1 KB instead. That’s what the approximate_size() function does.)

Look at the bottom of the script, and you’ll see two calls to print(approximate_size(arguments)). These are function calls — first calling the approximate_size() function and passing a number of arguments, then taking the return value and passing it straight on to the print() function. The print() function is built-in; you’ll never see an explicit declaration of it. You can just use it, anytime, anywhere. (There are lots of built-in functions, and lots more functions that are separated into modules. Patience, grasshopper.)

So why does running the script on the command line give you the same output every time? We’ll get to that. First, let’s look at that approximate_size() function.