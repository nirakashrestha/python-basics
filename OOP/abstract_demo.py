from abc import ABC, abstractmethod

#Abstract Class

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class Paypal(PaymentGateway):
    def pay(self):
        print("paying using Paypal...")

class RazorPay(PaymentGateway):
    def pay(self):
        print("paying using RazorPay...")

class Purchase:

    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("cheking out...")
        self.gateway.pay()


gateway1 = RazorPay()
gateway2 = Paypal()
purchase = Purchase(gateway2)
purchase.checkout()
