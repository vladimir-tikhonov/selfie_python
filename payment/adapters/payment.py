from transaction.models.transaction import Transaction

class Payment:
    def __init__(self, plan, customer, subscribee):
        self.plan = plan
        self.customer = customer
        self.subscribee = subscribee

    def process(self):
        transaction = Transaction(bill=123456, amount=self.plan.price)
        transaction.save()
        return transaction
