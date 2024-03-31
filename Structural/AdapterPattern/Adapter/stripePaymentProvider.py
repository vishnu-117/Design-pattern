from .adapter import PaymentProvider
from PaymentsApis.paymentapis import StripeApi

class StripeAdapter(PaymentProvider):
    global instance
    instance = StripeApi()

    def doPayment():
        return instance.createPayment()

    def getStatus(paymentId):
        return instance.getStatus(paymentId)
