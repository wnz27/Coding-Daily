from abc import ABCMeta, abstractmethod

# Subject
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

# RealSubject
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card  # Assume card number is account number
        return self.account
    
    def __hasFunds(self):  # 人为修改返回结果测试即可
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return False
    
    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

# Proxy
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    
    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()

# Client
class You:
    def __init__(self):
        print("You::Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None
    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()
    
    def __del__(self):
        if self.isPurchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")

you = You()
you.make_payment()

