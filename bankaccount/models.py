from django.db import models

# Create your models here.
class BankAccounts(models.Model):
    # return an integer field
    content = models.IntegerField('amount')
 

    def __int__(self):
        return  self.content
    

