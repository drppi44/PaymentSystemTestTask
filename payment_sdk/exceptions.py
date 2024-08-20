class PaymentException(Exception):
    def __init__(self, message='Payment Exception'):
        super().__init__(message)
