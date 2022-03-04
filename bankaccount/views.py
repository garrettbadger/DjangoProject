from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import BankAccounts
from django.db.models.functions import Cast
# Create your views here.

def set_up(request):
    all_bank_accounts = BankAccounts.objects.all()

    return render(request, 'setup.html', {'bank_accounts':all_bank_accounts})
    

def addBankAccount(request):
    all_bank_accounts = BankAccounts.objects.all()
    bank_balance = {'statements': all_bank_accounts}
    new_amount = BankAccounts(content = int(request.POST['amount']))
    
    new_amount.save()
    
    if request.POST['changing_funds'] == 'Deposit':
        new_amount += Cast('integer',bank_balance['statements'])
    else:
         new_amount -= Cast('integer',bank_balance['statements'])

    
    
    
    return HttpResponseRedirect('/bankaccount/')