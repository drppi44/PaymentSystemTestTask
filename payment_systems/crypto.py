from payment_systems.exceptions import ExceptionRaiser


class CryptoPayment(ExceptionRaiser):
    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def process_transaction(self, **kwargs):
        self.throw_error()
        print('Crypto payment success')

        return 0
