from asyncio.constants import ACCEPT_RETRY_DELAY
from time import time
from types import ClassMethodDescriptorType
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.TextField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=6)
    age=models.PositiveSmallIntegerField()
class Wallet(models.Model):
    currency=models.CharField(max_length=255, blank=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    balance=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=255, blank=True)
    pin=models.CharField(max_length=255, blank=True)
class Account(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    acc_type=models.CharField(max_length=255,null=True)
    account_number=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
class Transaction(models.Model):
    transaction_code=models.CharField(max_length=255)
    Wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField(null=True)
    transaction_date=models.DateField(auto_now_add=True,null=True)
    transaction__type=models.CharField(max_length=255,null=True)
    receipt=models.ForeignKey(Account,on_delete=models.CASCADE)
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    destination_account=models.ForeignKey(Account, on_delete=models.CASCADE)
class Card(models.Model):
    date_issued = models.DateTimeField(auto_now_add=True)
    card_name = models.CharField(max_length=255, blank=True)
    card_number = models.IntegerField(blank=True)
    card_type=models.CharField(max_length=255, blank=True)
    card_date = models.DateField(auto_now_add=True)
    card_status = models.CharField(max_length=255, blank=True)
    security_code = models.IntegerField(blank=True )
    wallet= models.ForeignKey(Wallet, on_delete=models.CASCADE)
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    issuer=models.CharField(max_length=255, blank=True)
class ThirdParty(models.Model):
    account=models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    id=models.CharField(max_length=255, blank=True)
    phone_number=models.CharField(max_length=255, blank=True)
class Notification(models.Model):
    id=models.PositiveSmallIntegerField(null=True, blank=True) 
    name=models.CharField(max_length=255, blank=True)
    status=models.CharField(max_length=255, blank=True)
    date=models.DateTimeField(null=True, blank=True)
    time=models.DateTimeField(max_length=255, blank=True)
    recepient=models.CharField(max_length=255, blank=True)
class Receipt(models.Model):    
    receipt_type=models.CharField(max_length=255, blank=True)
    receipt_date=models.DateField(max_length=255)
    receipt_file=models.FileField(max_length=255, blank=True)
    amount=models.IntegerField(max_length=255, blank=True)
    acc_number=models.IntegerField(max_length=255, blank=True)
    transaction=models.ForeignKey(Transaction)
class Loan(models.Model):
    loan_number=models.CharField(max_length=255, blank=True)
    loan_type=models.CharField(max_length=255, blank=True)
    amount=models.BigIntegerField(max_length=255, blank=True)
    date_time=models.DateTimeField(auto_now_add=True)
    wallet= models.ForeignKey(Wallet, on_delete=models.CASCADE)
    interest_rate=models.IntegerField(max_length=255, blank=True)
    guarantor=models.ForeignKey(Customer, on_delete=models.CASCADE)
    pay_due_date=models.DateField(auto_now_add=True)
    loan_balance=models.IntegerField(max_length=255, blank=True)
    loan_term=models.IntegerField(max_length=255, blank=True)
class Reward(models.Model):
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    date_and_time=models.DateField(auto_now_add=True)
    customer_id=models.IntegerField(max_length=255)
    gender=models.CharField(max_length=255)
    bonus=models.IntegerField(max_length=255)
