from .adapter import PaymentProvider
from PaymentsApis.paymentapis import Paypal


class PaypalAdapter(PaymentProvider):

    global instance
    instance = Paypal()

    def doPayment():
        return instance.makePayment()

    def getStatus(paymentId):
        return instance.checkstatus(paymentId)
