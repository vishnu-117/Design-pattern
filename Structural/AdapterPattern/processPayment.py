from Adapter.payPalPaymentProvider import PaypalAdapter
from Adapter.stripePaymentProvider import StripeAdapter

class PaymentProcessor:

    def __init__(self, PaymentProvider):
        self.PaymentProvider = PaymentProvider

    def processPayment(self):
        payment = self.PaymentProvider.doPayment()
        print(payment)
        status = self.PaymentProvider.getStatus(123)
        print(status)

instance = PaymentProcessor(PaypalAdapter)
instance.processPayment()
instance = PaymentProcessor(StripeAdapter)
instance.processPayment()

