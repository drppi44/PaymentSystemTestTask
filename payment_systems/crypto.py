import random

from payment_systems.exceptions import PaymentException


class CryptoPayment:
    # noinspection PyMethodMayBeStatic
    def process_transaction(self, **kwargs):
        self.throw_error()
        print('Crypto payment success')

        return 0

    @staticmethod
    def throw_error():
        if random.random() < 0.2:  # 20% chance of failure
            raise PaymentException()
