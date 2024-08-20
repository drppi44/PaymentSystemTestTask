from typing import Type

from payment_sdk.exceptions import PaymentException
from payment_sdk.payment_facades import PaymentFacade


class PaymentProcessor:
    """
        Class to process payments using a specified payment system.

        This class uses the provided payment facade to handle payments,
        and is responsible for managing exceptions during the payment
        process.

        Parameters
        ----------
        payment_system : PaymentFacade
            A concrete class that inherits from PaymentFacade, used to
            process payments.

        Methods
        -------
        process_payment(**kwargs)
            Processes a payment using the configured payment system.
            Raises a PaymentException if there is an error during the
            payment process.
        """
    def __init__(self, payment_system: Type[PaymentFacade]):
        """
        Initialize the PaymentProcessor with a specific payment facade.

        Parameters
        ----------
        payment_system : PaymentFacade
            A concrete class that inherits from PaymentFacade.
        """
        self.payment_system = payment_system()

    def process_payment(self, **kwargs):
        """
        Process a payment with the provided payment details.

        Parameters
        ----------
        **kwargs : dict
            Payment details required by the payment system.

        Raises
        ------
        PaymentException
            If there is an error during payment processing.
        """
        # noinspection PyBroadException
        try:
            self.payment_system.pay(**kwargs)
        except Exception as exc:
            raise PaymentException() from exc
