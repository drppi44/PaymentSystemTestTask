from payment_systems.exceptions import ExceptionRaiser


class CreditCardPayment(ExceptionRaiser):
    # noinspection PyMethodMayBeStatic
    def pay(self, **kwargs):
        self.throw_error()
        print('Credit card payment success')

        return 0
