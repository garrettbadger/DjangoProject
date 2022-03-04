from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import BankAccounts
from django.db.models.functions import Cast
# Create your views here.

def set_up(request):
    #collect all bankaccounts objects
    all_bank_accounts = BankAccounts.objects.all()
    #return the bankaccounts objects to the html in the form of a dictionary
    return render(request, 'setup.html', {'bank_accounts':all_bank_accounts})
    

def addBankAccount(request):
    #create another dictionary with all the bank account objects
    all_bank_accounts = BankAccounts.objects.all()
    bank_balance = {'statements': all_bank_accounts}
    #collect the amount of money from the html document provided by the user
    new_amount = BankAccounts(content = int(request.POST['amount']))
    #save it to the db
    new_amount.save()
    #if the radio button for deposit was selected then add the current amount to the previous one
    if request.POST['changing_funds'] == 'Deposit':
        new_amount += Cast('integer',bank_balance['statements'])
    #if the radio button for withdraw was selected then subtract the current amount from the previous one
    else:
         new_amount -= Cast('integer',bank_balance['statements'])
    #return to the html
    return HttpResponseRedirect('/bankaccount/')