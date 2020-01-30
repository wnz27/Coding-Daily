## 第四章 门面模式--与门面相适
这一章我们学习另外一种类型的设计模式，即结构型设计模式。

这里，我们要介绍的是门面设计模式，以及如何将其应用于软件应用程序开发。
本章讨论下列主题：
* 结构型设计模式概要
* 利用UML图理解门面设计模式
* 实现代码的真实用例
* 门面模式与最少知识原则
### 4.1 理解结构型设计模式
以下几点有助于我们更好了解结构型设计模式。
* 结构型模式描述如何将对象和类组合成更大的结构。
* 结构型模式是一种能够简化设计工作的模式，因为它能够找出更简单的方法来认识或
表示实体之间的关系。在面向对象世界中，实体指的是对象或类。
* 类模式可以通过继承来描述抽象，从而提供更有用的程序接口，而对象模式则描述了
如何将对象联系起来从而组合成更大的对象。结构型模式是类和对象模式的综合体。

下面给出结构型设计模式的几个例子。它们都是通过对象或类之间的交互来实现更高级的
设计或架构目标的。
* 适配器模式：将一个接口转换成客户希望的另外一个接口。它试图根据客户端的需求来
匹配不同类的接口
* 桥接模式：该模式将对象的接口与其实现进行解耦，使得两者可以独立工作。
* 装饰器模式：该模式允许在运行时或以动态的方式为对象添加职责。我们可以通过
接口给对象添加某些属性。

### 4.2 理解门面设计模式
门面（facade）通常是指建筑物的表面，尤其是最有吸引力的那一面。它也可以表示一种
容易让人误解某人的真实感受或情况的行为或面貌。当人们从建筑物外面经过时，可以欣赏
其外部面貌，却不了解建筑物结构的复杂性。这就是门面模式的使用方式。门面在隐藏内部
系统复杂性的同时，为客户端提供了一个接口，以便它们可以非常轻松地访问系统。

下面我们以店主为例进行介绍。现在假设你要到某个商店去买东西，但是你对这个商店的布局
并不清楚。通常情况下，你会去找店主，因为店主对整个商店都很清楚。只要你告诉他/她要买
什么，店主就会把这些商品拿给你。这不是很容易吗？顾客不必了解店面的情况，可以通过
一个简单的接口来完成购物，这里的接口就是店主。

门面设计模式实际上完成了下列事项：
* 它为子系统中的一组接口提供一个统一的接口，并定义一个高级接口来帮助客户端通过
更加简单的方式使用子系统。
* 门面所解决的问题是，如何用单个接口对象来表示复杂的子系统。实际上，它并不是
封装子系统，而是对底层子系统进行组合。
* 它促进了实现与多个客户端的解耦。

### 4.3 UML类图
借助UML图来深入探讨门面模式
![门面模式](../img/门面模式.png)
在图中看到，这个模式有三个主要的参与者
* 门面：门面主要责任是，将一组复杂系统封装起来，从而为外部世界提供一个舒适的外观。
* 系统：这代表一组不同的子系统，使整个系统混杂在一起，难以观察或使用。
* 客户端：客户端与门面进行交互，这样就可以轻松地与子系统进行通信并完成工作了。
不必担心系统的复杂性。

现在我们将会从数据结构的角度进一步介绍这3个主要参与者。
#### 4.3.1 门面
* 它是一个接口，它知道某个请求可以交由那个子系统进行处理。
* 它使用组合将客户端的请求委派给相应的子系统对象。

例如，如果客户端正在了解哪些工作已经完成，则不需要到各个子系统去，
相反，它只需要联系完成工作的接口（门面）就可以了。

#### 4.3.2 系统
在门面的世界里，系统就是执行以下操作的实体。
* 它实现子系统的功能，同时，系统由一个类表示。
理想情况下，系统应该由一组负责不同任务的类来表示。
* 它处理门面对象分配的工作，但并不知道门面，而且不引用它。

例如，当客户端向门面请求某项服务时，门面会根据服务的类型来选择提供该服务的相应子系统。

#### 4.3.3 客户端
以下是对客户端的描述。
* 客户端是实例化门面的类。
* 为了让子系统完成相应的工作，客户端需要向门面提出请求。

### 4.4 在显示世界中实现门面模式
举个生活中的例子。
假设你要在家中举行一场婚礼，并且由你来张罗这一切。这真是一个艰巨的任务。
你必须预定一家酒店或场地，与餐饮人员交代酒菜、布置场景，并且安排背景音乐。

在不久以前，你已经自己搞定了一切，例如找相关人员谈话、与他们进行协调、敲定价格等。
此外，你还可以去找会务经理，让他/她为你处理这些事情。
会务经理负责跟哥哥服务提供商交涉，并为你争取最优惠的价格。

下面我们从门面模式的角度来看待这些事情。
* 客户端：你需要在婚礼前及时完成所有的准备工作。每一项安排都应该是顶级的，
这样客人才会喜欢这些庆祝活动。
* 门面：会务经理负责与所有相关人员进行交涉，这些人员负责处理食物、花卉装饰等。
* 子系统：它们代表提供餐饮、酒店管理和花卉装饰等服务的系统。

现在，让我们利用Python开发一个应用程序，实现这个示例。我们首先从客户端开始。
记住，你是确保婚姻准备工作和事件顺利的总负责人。

接下来要谈论的的是Facade类。Facade类简化了客户端的接口。就本例来说，
EventManager扮演了门面的角色，并简化了你的工作。
Facade与子系统进行交流，并代表你为婚姻完成所有的预定和准备工作。
下面是EventManager类的Python代码：
```
# Facade 门面
class EventManager(object):
    def __init__(self):
        print("Event Manager::Let me talk to the folks\n")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()
```
现在我们已经搞定了门面和客户端，下面让我们开始深入了解子系统。

我们为这个应用场景开发了以下类。
* Hotelier类用于预定酒店。它有一个方法，用于检查当天是否有可预订的酒店（`__isAvailable`）
* Florist类负责花卉装饰。这个类提供了`setFlowerRequirements()`方法，
用于指定要使用哪些种类的花卉来装饰婚礼。
* Caterer类用于跟备办宴席者打交道，并负责安排餐饮。Caterer提供了一个公开的
`setCuisine()`方法，用来指定婚宴的菜肴类型。
* Musicina类用来安排婚礼的音乐，它使用`setMusicType()`方法来了解会务的音乐要求。

接下来，让我们去定义这些子系统。
```
# 子系统
class Hotelier(object):
    def __init__(self):
        print("Arrange the Hotel for Marriage? --")
    
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    
    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")

# 子系统
class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")
    
    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")
    
# 子系统
class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")
    
    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")

# 子系统
class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
    
    def setMusicType(self):
        print("Jazz and Classical will be played\n\n")
```
这些事都委托了会务经理，不是吗？我们现在来看看You类。
在本例中，创建了一个`EventManager`类的对象，这样经理就会通过与相关人员进行
交涉来筹备婚礼，而你则可以找个地方喝茶了。
```
class You(object):
    def __init__(self):
        print("You::Whoa! Marriage Arrangements??!!!")
    def askEventManager(self):
        print("You::Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")
```
以上输出：
```
You::Whoa! Marriage Arrangements??!!!
You::Let's Contact the Event Manager


Event Manager::Let me talk to the folks

Arrange the Hotel for Marriage? --
Is the Hotel free for the event on given day?
Registered the Booking


Flower Decorations for the Event? --
Carnations, Roses and Lilies would be used for Decorations


Food Arrangements for the Event --
Chinese & Continental Cuisine to be served


Musical Arrangements for the Marriage --
Jazz and Classical will be played


You:: Thanks to Event Manager, all preparations done! Phew!
```
[代码版本：Python v3.8.0](../相关代码/第四章/4.4.py)

我们可以通过以下方式将门面模式与真实世界场景相关联。
* EventManager类是简化接口的门面。
* EventManager通过组合创建子系统的对象，如Hotelier、Caterer等等。
### 4.5 最少知识原则
门面为我们提供了一个统一的系统，它使得子系统更加易于使用。它还将客户端与子系统解耦。
门面模式背后的设计原理就是最少知识原则。

最少知识原则知道我们减少对象之间的交互，就像跟你亲近的只有某几个朋友那样。
实际上，它意味着：
* 再设计系统时，对于创建的每个对象，都应该考察与之交互的类的数量，以及交互的方式
* 遵循这个原则，就能够避免创建许多彼此紧密耦合的类的情况。
* 如果类之间存在大量依赖关系，那么系统就会变得难以维护。如果对系统中的任何一部分进行修改，
都可能导致系统的其他部分被无意改变，这意味着系统会退化，是应该坚决避免的。

### 4.6 常见问答
Q1. 迪米特法则是什么，它与工厂模式有何关联？

A：迪米特法则是一个设计准则，涉及以下内容：
* 每个单元对系统中其他单元知道的越少越好
* 单位应该只与其朋友交流
* 单元不应该知道它操作的对象的内部细节

最少知识原则和迪米特法则是一致的，都是指向松耦合理论。就像它的名称所暗示的那样，
最少知识原则适用于门面模式的用例，并且“原则”这个词是指导方针的意思，
而不是严格遵守的意思，并且只在有需求的时候才用。

Q2. 子系统可以有多个门面吗？

A：是的，可以为一组子系统组件实现多个门面。

Q3. 最少知识原则的缺点是什么？

A：门面提供了一个简化的接口供客户端与子系统交互。本着提供简化接口的精神，
应用可能会建立多个不必要的接口，这增加了系统的复杂性并且降低了运行时的性能。

Q4. 客户端可以独立访问子系统吗？

A：是的，事实上，由于门面模式提供了简化的接口，这使得客户端不必担心子系统的复杂性。

Q5. 门面是否可以添加自己的功能？

A：门面可以将其“想法”添加到子系统中，例如确保子系统的改进顺序由门面来决定。