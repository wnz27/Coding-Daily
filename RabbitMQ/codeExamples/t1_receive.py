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
