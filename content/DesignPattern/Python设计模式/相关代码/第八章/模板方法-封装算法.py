'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-25 11:34:14
@LastEditTime: 2020-03-25 11:39:02
@FilePath: /Coding-Daily/content/DesignPattern/Python设计模式/相关代码/第八章/模板方法-封装算法.py
@description: type some description
'''
from abc import ABCMeta, abstractmethod

class AbstractClass(metacalss=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print("Defining the Algorithm. Operation1 follows Operation2")
        self.operation1()
        self.operation2()

class ConcreteClass(AbstractClass):
    def operation1(self):
        print("My Concrete Operation1")
    
    def operation2(self):
        print("Operation 2 remains same!")

class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()

client = Client()
client.main()