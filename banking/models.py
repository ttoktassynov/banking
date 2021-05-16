from django.db import models
from banking.helper import CreditDebitCodes, AccountStatuses
# Create your models here.

class Account(models.Model):
    identification = models.CharField(max_length=256)
    status = models.IntegerField(choices=AccountStatuses.choices(), default=AccountStatuses.ENABLED)
    name = models.CharField(max_length=350)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.identification
    
    def get_account_desc(self):
        return "{} of {} with {} units".format(
            self.identification, self.name, self.balance)
    def get_account_status_label(self):
        return AccountStatuses(self.type).name.title()

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 12, decimal_places=2)
    bookingDateTime = models.DateTimeField(auto_now=True)
    creditDebitIndicator = models.IntegerField(choices=CreditDebitCodes.choices(), default=CreditDebitCodes.CREDIT)
    creditorIdentification = models.CharField(max_length=256)
    debtorIdentification = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)

    def get_tran_desc(self):
        result = "{} {} on {} of {} units".format(self.id, 
            self.creditDebitIndicator,
            self.bookingDateTime,
            self.amount)
        if self.creditDebitIndicator == "Credit":
            result += " from {}".format(self.debtorIdentification)
        else:
            result += " to {}".format(self.creditorIdentification)
        return result
    def get_creditdebit_code_label(self):
        return CreditDebitCodes(self.type).name.title()