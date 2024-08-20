from abc import ABC
from abc import abstractmethod

from payment_systems.credit_card import CreditCardPayment
from payment_systems.crypto import CryptoPayment
from payment_systems.paypal import PaypalPayment


class PaymentFacade(ABC):
    """
    Abstract base class for payment facades.

    This class defines a common interface for different payment methods.
    Concrete implementations should provide specific payment processing
    logic for each payment method.

    Methods
    -------
    pay(**kwargs)
        Abstract method to process a payment. Concrete implementations
        must override this method to provide payment processing logic.
    """

    @abstractmethod
    def pay(self, **kwargs):
        """
        Process a payment with the provided parameters.

        Parameters
        ----------
        **kwargs : dict
            Payment details that are specific to the payment method.

        Raises
        ------
        NotImplementedError
            If the method is not overridden in a subclass.
        """
        ...


class PaypalFacade(PaymentFacade):
    """
    Concrete implementation of PaymentFacade for PayPal payments.

    This class uses the PayPal API to send money and processes payments
    through the PayPal payment system.

    Methods
    -------
    pay(**kwargs)
        Processes a payment using PayPal.
    """
    def pay(self, **kwargs):
        """
        Process a payment using PayPal.

        Parameters
        ----------
        **kwargs : dict
            Payment details required by the PayPal API.

        Raises
        ------
        Exception
            If there is an error during payment processing.
        """
        paypal_payment = PaypalPayment()
        paypal_payment.send_money(**kwargs)


class CryptoFacade(PaymentFacade):
    """
    Concrete implementation of PaymentFacade for Crypto payments.

    This class uses the Crypto API to process transactions through the
    cryptocurrency payment system.

    Methods
    -------
    pay(**kwargs)
        Processes a payment using cryptocurrency.
    """
    def pay(self, **kwargs):
        """
        Process a payment using cryptocurrency.

        Parameters
        ----------
        **kwargs : dict
            Payment details required by the Crypto API.

        Raises
        ------
        Exception
            If there is an error during payment processing.
        """
        crypto_payment = CryptoPayment()
        crypto_payment.process_transaction(**kwargs)


class CreditCardFacade(PaymentFacade):
    """
    Concrete implementation of PaymentFacade for Credit Card payments.

    This class uses the Credit Card API to process payments through the
    credit card payment system.

    Methods
    -------
    pay(**kwargs)
        Processes a payment using a credit card.
    """
    def pay(self, **kwargs):
        """
        Process a payment using a credit card.

        Parameters
        ----------
        **kwargs : dict
            Payment details required by the Credit Card API.

        Raises
        ------
        Exception
            If there is an error during payment processing.
        """
        credit_card_payment = CreditCardPayment()
        credit_card_payment.pay(**kwargs)
