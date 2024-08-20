class PaymentException(Exception):
    def __init__(self):
        super().__init__('Payment Exception')
