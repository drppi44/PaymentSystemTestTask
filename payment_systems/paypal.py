from payment_systems.exceptions import ExceptionRaiser


class PaypalPayment(ExceptionRaiser):
    # noinspection PyMethodMayBeStatic
    def send_money(self, **kwargs):
        self.throw_error()
        print('Paypal payment success')

        return 0
