'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-25 11:41:48
@LastEditTime: 2020-03-25 11:47:33
@FilePath: /Coding-Daily/content/DesignPattern/Python设计模式/相关代码/第十章/状态设计模式.py
@description: type some description
'''
from abc import abstractmethod, ABCMeta

class State(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self):
        pass

class ConcreteStateB(State):
    def Handle(self):
        print("my state is ConcreteStateB")

class ConcreteStateA(State):
    def Handle(self):
        print("my state is ConcreteStateA")

class Context(State):
    def __init__(self):
        self.state = None
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def Handle(self):
        self.state.Handle()

context = Context()
stateA = ConcreteStateA()
stataB = ConcreteStateB()

context.setState(stateA)
context.Handle()