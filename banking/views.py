from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from banking.models import Account, Transaction
from django.views import generic
from django.template import loader
from django.urls import reverse
from banking.helper import CreditDebitCodes

class IndexView(generic.ListView):
    template_name = 'banking/index.html'
    context_object_name = 'account_list'

    def get_queryset(self):
        """Return all accounts"""
        return Account.objects.all()

class HistoryView(generic.ListView):
    template_name = 'banking/history.html'
    context_object_name = 'latest_transactions_list'
    
    def get_queryset(self):
        self.account = get_object_or_404(Account, id=self.kwargs['pk'])
        return Transaction.objects.filter(account=self.account).order_by('-bookingDateTime')[:5]


def pay(request, accountId):
    account = get_object_or_404(Account, pk=accountId)
    if request.method == "GET":
        return render(request, 'banking/pay.html', {
            'account': account
        })
    elif request.method == "POST":
        amount = float(request.POST['amount'])
        creditDebitIndicator = int(request.POST['creditdebitCode'])
        counterAccIdentification = request.POST["identification"]
        creditorIdentification = account.identification
        debtorIdentification = counterAccIdentification

        if creditDebitIndicator == CreditDebitCodes.DEBIT:
            creditorIdentification = counterAccIdentification
            debtorIdentification = account.identification

        transaction = account.transaction_set.create(
            amount = amount,
            creditDebitIndicator = creditDebitIndicator,
            creditorIdentification = creditorIdentification,
            debtorIdentification = debtorIdentification
        )

        return HttpResponseRedirect(reverse('banking:history', args=(account.id,)))