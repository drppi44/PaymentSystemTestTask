from abc import ABC

from payment_systems.crypto import CryptoPayment
from payment_systems.credit_card import CreditCardPayment
from payment_systems.paypal import PaypalPayment


class PaymentFacade(ABC):
    def pay(self, **kwargs):
        raise NotImplementedError


class PaypalFacade(PaymentFacade):
    def pay(self, **kwargs):
        paypal_payment = PaypalPayment()
        paypal_payment.send_money(**kwargs)

        print('Paypal payment success')


class CryptoFacade(PaymentFacade):
    def pay(self, **kwargs):
        crypto_payment = CryptoPayment()
        crypto_payment.process_transaction(**kwargs)

        print('Crypto payment success')


class CreditCardFacade(PaymentFacade):
    def pay(self, **kwargs):
        credit_card_payment = CreditCardPayment()
        credit_card_payment.pay(**kwargs)

        print('Credit card payment success')
