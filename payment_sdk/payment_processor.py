import random
from typing import Type

from payment_sdk.payment_facades import PaymentFacade
from payment_systems.exceptions import PaymentException


class PaymentProcessor:
    def __init__(self, payment_system: Type[PaymentFacade]):
        self.payment_system = payment_system()

    def process_payment(self, **kwargs):
        # noinspection PyBroadException
        try:
            self.payment_system.pay(**kwargs)
        except PaymentException:
            print('Payment processing failed')
