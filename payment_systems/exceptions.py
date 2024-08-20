import random


class PaymentException(Exception):
    def __init__(self):
        super().__init__('Unexpected payment exception')


class ExceptionRaiser:
    @staticmethod
    def throw_error():
        if random.random() < 0.2:  # 20% chance of failure
            raise PaymentException()
