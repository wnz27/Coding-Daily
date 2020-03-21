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
