from payment.adapters.payment import Payment
from transaction.models.transaction import Transaction

class PaymentAdapter():
    @staticmethod
    def get_payment_page():
        return 'payment/new_payment.html'

    @staticmethod
    def create_payment(plan, customer, subscribee):
        return Payment(plan, customer, subscribee)

    @staticmethod
    def get_report_data(start, end):
        return Transaction.objects.filter(date__gt=start, date__lt=end)
