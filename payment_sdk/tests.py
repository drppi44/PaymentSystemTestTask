import unittest
from unittest.mock import patch

from payment_sdk.payment_facades import CreditCardFacade
from payment_sdk.payment_facades import CryptoFacade
from payment_sdk.payment_facades import PaypalFacade
from payment_sdk.payment_processor import PaymentProcessor


class TestPaymentProcessor(unittest.TestCase):
    @patch('payment_sdk.payment_facades.CreditCardPayment.pay')
    def test_credit_card_payment(self, mocked_method):
        processor = PaymentProcessor(CreditCardFacade)
        processor.process_payment()

        mocked_method.assert_called_once()

    @patch('payment_sdk.payment_facades.PaypalPayment.send_money')
    def test_paypal_payment(self, mocked_method):
        processor = PaymentProcessor(PaypalFacade)
        processor.process_payment()

        mocked_method.assert_called_once()

    @patch('payment_sdk.payment_facades.CryptoPayment.process_transaction')
    def test_crypto_payment(self, mocked_method):
        processor = PaymentProcessor(CryptoFacade)
        processor.process_payment()

        mocked_method.assert_called_once()
