from abc import ABCMeta, abstractmethod

# 具有抽象方法的类就是接口类，
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        """
        抽象方法，在实现的类中必须实现的方法。限制实现接口的类必须按照接口给定的调用方式实现这些方法
        :param money:
        :return:
        """
        pass

# 不能说是继承接口类，应该说是实现接口
class Alipay(Payment):
    def pay(self, money):
        """
        实现接口类中的必须实现的方法
        :param money:
        :return:
        """
        print("支付宝支付了{0}元!".format(money))

class WechatPay(Payment):
    def pay(self, money):
        """
        实现接口类中的必须实现的方法
        :param money:
        :return:
        """
        print("微信支付了%d元!" % (money))

# 下面是高层代码，在调用的时候是看不到底层类的内部实现
a = Alipay()
w = WechatPay()
a.pay(100)
w.pay(100)