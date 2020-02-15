## 第七章 命令模式--封装调用
本章中，讨论命令设计模式。就像观察者模式一样，命令模式也属于行为模式的范畴。
先介绍它，再讨论如何在软件应用程序开发中应用它。然后一个用例。
本章介绍如下主题：
* 命令模式简介
* 命令模式及其UML图
* Python 3.8 代码实现的用例
* 命令模式的优缺点
* 常见问答

### 7.1 命令设计模式简介
如上一章所看到的那样，行为模式侧重于对象的响应性。它利用对象之间的交互实现更强大的功能。
命令模式也是一种行为设计模式，其中对象用于封装在完成一项操作时或在触发一个事件时所需的
全部信息。这些信息包含以下内容：
* 方法名称
* 拥有方法的对象
* 方法参数的值

让我们用一个非常简单的软件例子来理解该模式，如安装向导。
通常情况下，安装向导通过多个步骤或屏幕来了解用户的偏好。
因此，当用户使用向导时，他/她需要作出某些选择。通常来说，向导可以使用命令模式来实现。
向导会首先启动一个名为Command的对象。
用户在向导的多个步骤中指定首选项或选项将存储在Command对象中。
当用户在向导的最后一个屏幕上单机Finish按钮时，Command对象就会运行`execute()`方法，
该方法会考察所有存储的选项并完成相应的安装过程。
因此，关于选择的所有信息被封装在稍后用于采取动作的对象中。

另一个简单的例子是打印机后台处理程序。假脱机程序可以用Command对象的形式来实现，
该对象用于存储页面类型（A5-A1）、纵向/横向、分选/不分选等信息。
当用户打印东西（例如图像）时，假脱机程序就会运行Command对象的`execute()`方法，
并使用设置的首选项打印图像。

### 7.2 了解命令设计模式
命令模式通常使用以下术语：Command、Receiver、Invoker和Client
* Command对象了解Receiver对象的情况，并能调用Receiver对象的方法
* 调用者方法的参数值存储在Command对象中
* 调用者知道如何执行命令
* 客户端用来创建Command对象并设置其接收者

命令模式的主要意图如下：
* 将请求封装为对象
* 可用不同的请求对客户进行参数化
* 允许将请求保存在队列中
* 提供面向对象的回调

命令模式可用于以下各种情景：
* 根据需要执行的操作对对象进行参数化
* 将操作添加到队列并在不同地点执行请求
* 创建一个结构来根据较小操作完成高级操作

假设我们要开发一个安装向导，或者更常见的安装程序。通常，
安装意味着需要根据用户做出的选择来复制或移动文件系统中的文件。
在下面示例中，我们首先在客户端代码中创建`Wizard`对象，
然后使用`preferences()`方法存储用户在向导的各个屏幕期间做出的选择。
在向导中单机Finish按钮时，就会调用`execute()`方法。
之后，`execute()`方法将会根据首选项来开始安装：
```
#! -*- conding=utf-8 -*-
class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src
    
    def preferences(self, command):
        self.choices.append(command)
    
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, "to", self.rootdir)
            else:
                print("No Operation")
    
if __name__ == "__main__":
    ## Client code
    wizard = Wizard("python 3.8.gizp", "/usr/bin/")
    ## Users chooses to install Python only
    wizard.preferences({'python':True})
    wizard.preferences({'java':False})
    wizard.execute()
```
上述代码的输出如下：
```
Copying binaries -- python 3.8.gizp to /usr/bin/
No Operation
```
[代码版本：Python v3.8.0](../相关代码/第七章/7.2.py)
#### 命令模式的UML类图
命令模式的主要参与者为：Command、ConcreteCommand、Receiver、Invoker、Client。

让我们看UML图，这些类是如何交互的
![]()
通过UML类图不难发现，该模式主要涉及5个参与者。
* Command：声明执行操作的接口。
* ConcreteCommand：讲一个Receiver对象和一个操作绑定在一起。
* Client：创建ConcreteCommand对象并设定其接收者。
* Invoker：要求该ConcreteCommand执行这个请求。
* 

[代码版本：Python v3.8.0](../相关代码/第七章/7.2.uml.py)
