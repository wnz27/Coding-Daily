## 第六章 观察者模式--了解对象的情况
本章中，我们讨论第三种类型的设计模式：行为型设计模式。
本章将介绍观察者模式，它就是一种行为型模式。
也将讨论如何在软件应用开发中使用观察者设计模式。

本章讨论以下主题：
* 行为涉及模式简介
* 观察者模式及其UML图
* 利用Python代码实现真实用例
* 松耦合的强大威力
* 常见问答

### 6.1 行为型模式简介
创建型模式的工作原理是基于对象的创建机制的。由于这些模式隔离了对象的创建细节，
所以使得代码能够与要创建的对象的类型相互独立。

结构型模式用于设计对象和类的结构，从而使它们可以相互协作以获得更大的结构。
它们重点关注的是简化结构以及识别类和对象之间的关系。

行为模式，顾名思义，它主要关注的是对象的责任。它们用来处理对象之间的交互，
以实现更大的功能。行为型模式建议：对象之间应该能够彼此交互，同时还应该是松散耦合的。
本章稍后会介绍松耦合的原理。

观察者设计模式是最简单的行为型模式之一，所以我们从它入手。学习这类模式。

### 6.2 理解观察者设计模式
在观察者模式中，对象（主题）维护了一个依赖（观察者）列表，以便主题可以使用观察者
定义的任何方法通知所有观察者它所发生的变化。

在分布式应用的世界中，多个服务通常是通过彼此交互来实现用户想要实现的更大型的操作的。
服务可以执行多种操作，但是它们执行的操作会直接或很大程度上取决于与其交互的服务对象的状态。

关于用户注册的示例，其中用户服务负责用户在网站上的各种操作。
假设我们有另一个称为电子邮件服务的服务，它的作用是监视用户的状态并向用户发送电子邮件。
例如，如果用户刚刚注册，则用户服务将调用电子邮件服务的方法，该方法将向用户发送电子邮件以进行账户验证。
如果账户经过了验证，但信用度较低，则电子邮件服务将监视用户服务并向用户发送信用度过低的电子邮件警报。

因此，如果在应用中存在一个许多其他服务所依赖的核心服务，那么该核心服务就会成为观察者
必须观察/监视其变化的主题。当主题发生变化时，观察者应该改变自己的对象的状态，或者采取某些动作。
这种情况（其中从属服务监视核心服务的状态变化）描述了观察者设计模式的经典情景。

在广播或发布/订阅系统的情形中，你会看到观察者设计模式的用法。
我们不妨考虑博客的例子，假设你是一个技术爱好者，喜欢阅读这个博客中Python方面的最新文章。
这时你会怎么做？当然是订阅该博客。许多其他订阅者也会在这个博客中注册。
所以，每当发布新博客时，你就会收到通知，或者如果原来的博客发生了变化，你也会收到通知。
当然，通知你发生改变的方式可以是电子邮件。
现在，如果将此场景应用于观察者模式，那么这里的博客就是维护订阅者或者观察者列表的主题。

因此，当有新的文章添加到博客中时，所有观察者就会通过电子邮件或由观察者定义任何
其他通知机制收到相应的通知。

观察者模式的主要目标如下：
* 它定义了对象之间的一对多的依赖关系，从而使得一个对象中的任何更改
都将自动通知给其他依赖对象
* 它封装了主题的核心组件。

观察者模式可以用于以下多种场景：
* 分布式系统中实现事件服务
* 用作新闻机构的框架
* 股票市场也是观察者模式的一个大型场景。

下面是观察者设计模式的Python实现：
```
class Subject:
    def __init__(self):
        self.__observers = []
    
    def register(self, observer):
        self.__observers.append(observer)
    
    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)

class Observer2:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)

subject = Subject()
ob1 = Observer1(subject)
ob2 = Observer2(subject)
subject.notifyAll('notification')
```
输出如下：
```
Observer1 :: Got ('notification',) From <__main__.Subject object at 0x108c6faf0>
Observer2 :: Got ('notification',) From <__main__.Subject object at 0x108c6faf0>
```
#### 观察者模式的UML类图
观察者模式主要有两个角色：主题和观察者。
让我们把这些角色放在一个UML图中，看看这些类如何交互的。
![观察者模式UML图]()
通过观察这个UML图可以发现，这个模式有3个主要角色。
* 主题（Subject）：类Subject需要了解Observer。Subject类具有许多方法，
诸如register()和deregister()等，Observer可以通过这些方法注册到Subject类中。
因此，一个Subject可以处理多个Observer。
* 观察者（Observer）：它为关注主题的对象定义了一个接口。它定义了Observer需要
实现的各个方法，以便在主题发生变化时能获得相应的通知。
* 具体观察者（ConcreteObserver）：它用来保存应该与Subject的状态保持一致的状态。
它实现了Observer接口以保持其状态与主题中的变化相一致。

这个流程非常简单，具体观察者通过实现观察者提供的接口向主题注册自己。
每当状态发生变化的时候，该主题都会使用观察者提供的通知方法来通告所有具体观察者。
### 6.3 现实世界中的观察者模式
我们将以新闻机构为例来展示观察者模式的现实世界场景。
新闻机构通常从不同地点收集新闻，并将其发布给订阅者。
下面我们来看看这个用例的设计注意事项。

由于信息是实时发送或者接收的，所以新闻机构应该尽快向其订阅用户公布该消息。
此外，随着技术的进步，订阅用户不仅可以订阅报纸，而且可以通过其他的形式进行订阅，
例如电子邮件、移动设备、短信、或语音呼叫。所以，我们还应该具备在将来添加任意其他
订阅形式的能力，以便为未来的新技术做好准备。

让我们用Python来开发一个应用程序，实现上面的用例。
我们将从主题开始，这里的主题是新闻发布者：
* 主题的行为由NewsPublisher类表示
* Newspublisher提供了一个供订阅用户使用的接口
* `attach()`方法供观察者(Observer)来注册NewsPublisherObserver
`detach()`方法用于注销
* `subscriber()`方法返回已经使用NewsPublisher注册的所有用户的列表
* `notifySubscriber()`方法可以用来遍历一已向NewsPublisher注册的所有订阅用户，执行某些操作。
* 发布者可以使用`addNews()`方法创建新消息，getNews()用于返回最新消息，并通知观察者。

现在我们来考察一下NewsPublisher类：
```
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    
    def addNews(self, news):
        self.__latestNews = news
    
    def getNews(self):
        return "Got News:", self.__latestNews
```
现在我们来讨论观察者（Observer）接口：
* 


