class Paypal:

    def __init__(self):
        pass

    def makePayment(self):
        return "Payment is Successfully done"

    def checkstatus(self, PaymentId):
        return "Done"

class StripeApi:

    def createPayment(self, request=None):
        return "Payment is captured"

    def getStatus(self, PaymetId):
        return "Ok"

    