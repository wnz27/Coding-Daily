from abc import ABCMeta, abstractmethod
#  Command
class Order(metaclass= ABCMeta):
    @abstractmethod
    def execute(self):
        pass

# ConcreteCommand1
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()

# ConcreteCommand2
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.sell()

# Receiver(命令实际执行者)
class StockTrade:
    def buy(self):
        print("You will buy stock!!!")
    
    def sell(self):
        print("Yout will sell stock!!!")
    
# Invoker（命令的调用者）
class Agent:
    def __init__(self):
        self.__orderQueue = []
    
    def placeOrder(self, order):
        self.__orderQueue.append(order)
    
    def execute(self):
        for order in self.__orderQueue:
            order.execute()

if __name__ == "__main__":
    # Client
    stock = StockTrade()
    buyStockOrder = BuyStockOrder(stock)
    sellStockOrder = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.placeOrder(buyStockOrder)
    agent.placeOrder(sellStockOrder)
    agent.execute()