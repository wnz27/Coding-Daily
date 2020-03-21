简单说明：
假设你装好RabbitMQ运行在localhost，端口默认的是5672，
如果你使用不一样的，那么需要调整。
## Tutorial 1------Hello World
RabbitMQ是一个消息代理，它接收和发送消息。

你可以把它想象成一个邮局，比如你想要寄信，你会把信件放进邮箱，
你知道邮递员会帮你把它送到你希望的人。类比这个，那么RabbitMQ就是
邮局，邮递员，邮箱。

而RabbitMQ和邮局不同的是，它不处理纸张，它接收，存储和发送的是
一些二进制的数据，也就是我们的信息。

用术语来解释一下：
- *Producer*：发送者/生产者，发送消息的程序一般被称为生产者。
![Producer](../img/Producer.jpg)
- *queue*：队列，这个就可以理解为RabbitMQ的邮箱，尽管消息经过RabbitMQ和你的应用程序，
但是消息只能被存储在队列里，一个队列的大小仅受主机的内存和磁盘的限制，可以把它理解为一个
较大的消息缓冲区。很多生产者可以往一个队列里发送消息，反过来，很多消费者也可以同时尝试
从一个队列里获得消息。
![queue](../img/queue.jpg)
- *Consumer*：接受者/消费者，主要等待消息的程序是消费者。
![Consumer](../img/consumer.jpg)

**注意：**
代理，生产者，消费者可以不在一个主机上，事实上很多应用也确实如此。
一个应用也同时可以做生产者和消费者。

### 使用Python的Pika客户端工具
教程这部分我们会用python写两个程序

一个生产者发送一个简单消息和一个消费者接受消息然后打印出来，这个消息是“Hello World”。
下面这个图，P就是生产者，C是消费者，中间那个盒子就是队列--代表消费者的消息缓冲区。
![简单消息队列图](../img/trans_mesage.jpg)

总体设计如下：生产者将消息发送到名叫hello的队列，消费者将从队列里接收到消息。

然后使用pip安装pika

### Sending
第一个程序`send.py`是要发送单个信息到队列里，要做的第一件事是与
RabbitMQ的服务器建立连接。
```
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
```
现在连接好了本地机器也就是`localhost`作为代理。如果要连接其他的机器作为代理，
只需简单的在参数位置指定名字或者IP地址就行了。

下一步必须确认接收消息的队列是存在的，如果我们把消息发送给一个不存在队列，
那么RabbitMQ将会把消息丢掉。

现在创建一个叫`hello`的队列，使得消息可以传递进去：
```
channel.queue_declare(queue='hello')
```
现在已经准备好发送消息了，第一个消息将仅仅包含一个字符串“Hello World!”。
并且我们想把它发送到hello这个队列里。

在RabbitMQ中，一个消息不能直接的发送到队列里，它需要经过`exchange`这个东西。
但是我们现在不扩展`exchange`的细节，将会在Tutorial3中知道更多一些。

现在只需要知道如何通过一个空字符串使用默认的`exchange`标识。此时，
这个`exchange`是特殊的，它允许我们指出消息应该去的确切的队列是哪一个。
这里把**队列的名字（字符串）**赋值给`routing_key`这个参数。
```
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!'
)
print("[x] Sent 'Hello World!'")
```
在退出程序之前，需要确保刷新了网络缓冲区，并且确认已将我们的消息传递到RabbitMQ。
我们可以通过关闭连接来实现。
```
connection.close()
```
#### 注意Sending不工作可能的原因
>也许是代理启动的时候没有足够的磁盘空间（默认它需要至少200MB空间）因此拒绝接收消息。
>可以检查代理的日志文件如果有必要的话可以减少这个限制。
>[在这里](https://www.rabbitmq.com/configure.html#config-items)你会知道
>如何设置`disk_free_limit`这个参数。

### Receiving
第二个程序是`receive.py`，这个程序将会从队列里获得消息，并把这个信息打印到屏幕上。
这时候再一次需要连接到RabbitMQ服务器，负责连接的代码与上面的是一样的。

再下一步，也是跟之前一样，我们必须确认队列是存在的。

需要说明的是：之前使用创建队列的方法`queue_declare`是幂等的，只要愿意我们可以多次运行这个
方法，它就只会创建一个队列。
>解释一下幂等：在编程中一个幂等操作的特点是其任意多次执行所产生的影响均与一次执行的影响相同。
```
channel.queue_declare(queue='hello')
```
也许会奇怪，为什么再次声明这个队列，之前我们已经声明过了，如果我们确定它存在，那这句代码
也许可以避免重复，比如send.py这个程序先运行。但是我们并不能在实际情况中哪个程序先运行。
所以在实际情况中我们在两个程序里都声明这个队列是一个很实用的技巧。

>**查看服务器的队列信息**

>如果需要查看现在RabbitMQ服务器有什么队列，以及有多少消息在这些队列里，那么可以用特权用户
>使用`rabbitmqctl`工具：
>```
>sudo rabbitmqctl list_queues
>```
>在Windows上，把以下输入，省略sudo：
>```
>rabbitmqctl.bat list_queues
>```

从队列接收接收消息要复杂一些。它通过向队列订阅回调函数来实现。

无论什么时候收到消息，这个回调函数就会被Pika这个库调用。
在我们的示例代码中，这个函数的功能是把消息打印到屏幕上。
```
def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
```
下一步，需要告诉RabbitMQ服务器，这个回调函数要从名叫hello的队列里接收消息。
```
channal.basic_consume(
    queue='hello', 
    auto_ack=True, 
    on_message_callback=callback
)
```
因为我们使用`queue_declare`再次声明过队列，所以可以肯定它绝对存在。
在下一节讨论`auto_ack`这个参数的一些细节。

最后定义一个死循环一直等待消息数据。
```
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```
最后把这个两个程序的代码贴出来。
[`send.py`源代码](../codeExamples/t1_send.py)
```
import pika

# 创建连接，主机为localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 为连接创建通道
channel = connection.channel()

# 声明队列，名称为hello
channel.queue_declare(queue='hello')

# 发送消息，exchange参数，为空字符串时要用routing_key来指出哪个队列，参数body指出消息的主体。
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!'
)
print("[x] Send 'Hello World!'")

# 关闭连接
connection.close()
```
[`receive.py`源代码](../codeExamples/t1_receive.py)
```
import pika

# 创建连接，主机为localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 为连接创建通道
channal = connection.channel()

# 声明队列，名称为hello
channal.queue_declare('hello')

# 给消费者定义回调函数，当接收到消息就会自动调用的函数
def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
# 给名叫hello的队列绑定回调函数，接收到了这个队列里的消息时自动调用回调函数
channal.basic_consume(
    queue='hello', 
    auto_ack=True, 
    on_message_callback=callback
)
print(" [*] Waiting for messages. To exit press CTRL+C")
# 建立死循环一直等待消息
channal.start_consuming()
```
在终端运行程序试一试，先运行接收者也就是消费者，它会持续等待传递。
```
python3 receive.py
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'Hello World!'
```
另一边，再打开一个终端窗口，运行`send.py`，这里我是python3来运行，也许你只用python即可。
注意，每次执行完生产者，这个程序自动停掉。
```
python3 send.py
# => [x] Sent 'Hello World!'
```
你运行完就会注意到，接收者也就是消费者的程序没有停止。它继续做好准备接收消息，你可以用不断运行
`send.py`程序看到接收者那边可以一直收到消息，需要用CTRL+C来把消费者停止。

现在我们学会了如何从一个指定名字的队列里获得消息，接下来我们去[下一章](./Tutorial-2-WorkQueues.md)学习建立一个简单的工作队列。







