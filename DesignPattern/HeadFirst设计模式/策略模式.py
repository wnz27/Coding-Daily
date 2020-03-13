'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-13 08:52:29
@LastEditTime: 2020-03-13 09:38:55
@FilePath: /Coding-Daily/DesignPattern/HeadFirst设计模式/策略模式.py
@description: type some description
'''
from abc import ABCMeta, abstractmethod
# 书上demo
class Duck(metaclass=ABCMeta):
    def __init__(self, flybehaviour, quackbehaviour):
        self.flybehaviour = flybehaviour
        self.quackhabiour = quackbehaviour
    
    def swim(self):
        print("All duck float!")

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.flybehaviour.fly()
    
    def performQuack(self):
        self.quackhabiour.quack()
    
    def setFlyBehaviour(self, newBehaviour):
        self.flybehaviour = newBehaviour
    
    def setQuackBehaviour(self, newBehaviour):
        self.quackhabiour = newBehaviour
    
class FlyBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class QuackBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

'''
游戏状态切换，攻击行为发生不同的变化
'''
    
    