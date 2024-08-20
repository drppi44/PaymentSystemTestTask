# Payment Processing SDK

This SDK provides a simple interface for processing payments using various payment methods such as PayPal, Crypto, and
Credit Cards. The SDK abstracts the complexity of integrating with different payment gateways and offers a unified API
for handling payments.

## Features

- **Multiple Payment Methods**: Supports payments via PayPal, Crypto, and Credit Cards.
- **Facade Pattern**: Simplifies the integration by providing a common interface for all payment methods.
- **Customizable**: Easily extendable to support additional payment methods.
- **ABC**: Uses Abstraction
- **Type hint**: Extra features for better static code analyze
- **Tests**: Covered by tests
- **PEP8**: compatible

## Installation

To install the SDK, clone the repository, doesn't require any pip libs:

```bash
git clone https://github.com/drppi44/PaymentSystemTestTask.git
```

## Usage

```python
from payment_sdk.payment_processor import PaymentProcessor
from payment_sdk.payment_facades import PaypalFacade

# Create an instance of the PaymentProcessor
# with given payment system
processor = PaymentProcessor(PaypalFacade)

# Pay using PayPal
processor.process_payment(
    amount=100.0,
    currency='USD',
    recipient_email='recipient@example.com'
)

# Expected output: "Paypal payment success"
```