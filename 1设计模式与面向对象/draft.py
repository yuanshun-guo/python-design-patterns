# 第一种写法
# class Payment:
#     def pay(self, money):
#         """若继承的类没有调用pay方法，就会出发这个类，从而raise一个错误"""
#         raise NotImplementedError
#
# class Alipay(Payment):
#     def pay(self, money):
#         pass
#
# class Wechat(Payment):
#     def pay(self, money):
#         pass
#
# p = Alipay()
# p.pay(100)

# 第二种写法
from abc import ABCMeta, abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        """
        所有继承这个Payment类的，都需要实现pay这个方法，否则会引发错误
        若调用了，这会覆盖这个方法，从而不会引发错误
        """
        pass

class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元"%money)

class Wechat(Payment):
    def pay(self, money):
        print(f"支付宝支付{money}元")

p = Alipay()
p.pay(100)