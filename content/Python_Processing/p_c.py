# -*- coding: utf-8 -*-
# @UpdateTime    : 2023/7/6 00:18
# @Author    : 27
# @File    : p_c.py.py

import multiprocessing, time, random


class producer(multiprocessing.Process):
    def __init__(self, queue: multiprocessing.Queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            # item = random.randint(0, 256)
            item = i + 1
            self.queue.put(item)
            print("Process Producer: item {} append to queue {}".format(item, self.name))
            time.sleep(1)
            print("The size of queue is {}".format(self.queue.qsize()))


class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print("Process Consumer: item {} popped from by {}".format(item, self.name))

                time.sleep(1)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
    pass
