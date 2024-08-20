import random

from payment_systems.exceptions import PaymentException


class PaypalPayment:
    # noinspection PyMethodMayBeStatic
    def send_money(self, **kwargs):
        self.throw_error()
        print('Paypal payment success')

        return 0

    @staticmethod
    def throw_error():
        if random.random() < 0.2:  # 20% chance of failure
            raise PaymentException()
