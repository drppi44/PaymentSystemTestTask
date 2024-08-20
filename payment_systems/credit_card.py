import random

from payment_systems.exceptions import PaymentException


class CreditCardPayment:
    # noinspection PyMethodMayBeStatic
    def pay(self, **kwargs):
        self.throw_error()
        print('Credit card payment success')

        return 0

    @staticmethod
    def throw_error():
        if random.random() < 0.2:  # 20% chance of failure
            raise PaymentException()
