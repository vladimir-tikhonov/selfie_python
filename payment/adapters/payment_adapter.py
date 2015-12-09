from payment.adapters.payment import Payment

class PaymentAdapter():
    @staticmethod
    def get_payment_page():
        return 'payment/new_payment.html'

    @staticmethod
    def create_payment(plan, customer, subscribee):
        return Payment(plan, customer, subscribee)
