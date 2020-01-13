# RabbitMQ for python 学习记录

## Part1
#### Jargon
* Producing means nothing more than sending. A program that sends messages is a producer
* A queue is the name for a post box which lives inside RabbitMQ. Although messages flow through RabbitMQ and your applications, they can only be stored inside a queue. A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer. Many producers can send messages that go to one queue, and many consumers can try to receive data from one queue.
* Consuming has a similar meaning to receiving. A consumer is a program that mostly waits to receive messages

### RabbitMQ libraries
RabbitMQ speaks multiple protocols. This tutorial uses AMQP 0-9-1, which is an open, general-purpose protocol for messaging. 
There are a number of clients for RabbitMQ in many different languages. 

In this tutorial series we're going to use Pika 1.0.0, which is the Python client recommended by the RabbitMQ team. To install it you can use the pip package management tool:

`python -m pip install pika --upgrade`

### Attention
before sending we need to make sure the recipient queue exists. 
If we send a message to non-existing location, RabbitMQ will just drop the message. 
Let's create a hello queue to which the message will be delivered:
`channel.queue_declare(queue='hello')`
and in the receive.py ,is to make sure that the queue exists. 
Creating a queue using queue_declare is idempotent ‒ we can run the command as many times as we like, and only one will be created.
because that command List queues which `sudo rabbitmqctl list_queues` to succeed 
we must be sure that a queue which we want to subscribe to exists. 
Fortunately we're confident about that ‒ we've created a queue above ‒ using queue_declare.
###### Listing queues
You may wish to see what queues RabbitMQ has and how many messages are in them.
You can do it (as a privileged user) using the rabbitmqctl tool:
`sudo rabbitmqctl list_queues`
On Windows, omit the sudo:
`rabbitmqctl.bat list_queues`
##### Sending doesn't work!
If this is your first time using RabbitMQ and you don't see the "Sent" message 
then you may be left scratching your head wondering what could be wrong. 
Maybe the broker was started without enough free disk space (by default it needs at least 200 MB free) and is therefore refusing to accept messages. 
Check the broker logfile to confirm and reduce the limit if necessary. 
The configuration file documentation will show you how to set disk_free_limit.




