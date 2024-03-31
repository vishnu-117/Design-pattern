class StripeApi:

    def createPayment(self):
        return "Payment is captured"

    def getStatus(self, PaymetId):
        return "Ok"

class Paypal:

    def makePayment(self):
        return "Payment is Successfully done"

    def getstatus(self, paymentId):
        return "Done"