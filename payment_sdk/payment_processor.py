import random
from typing import Type

from payment_sdk.payment_facades import PaymentFacade


class PaymentProcessor:
    def __init__(self, payment_system: Type[PaymentFacade]):
        self.payment_system = payment_system()

    def process_payment(self, **kwargs):
        # noinspection PyBroadException
        try:
            self.throw_error()

            self.payment_system.pay(**kwargs)
        except Exception:
            print('Payment processing failed')

    @staticmethod
    def throw_error():
        if random.random() < 0.2:  # 20% chance of failure
            raise Exception("Random payment processing error")
