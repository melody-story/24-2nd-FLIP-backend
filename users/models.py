from django.db import models

class User(models.Model):
    kakao_id        = models.IntegerField()
    email           = models.CharField(max_length=100, null=True)
    password        = models.CharField(max_length=2000, null=True)
    nickname        = models.CharField(max_length=100)
    image_url       = models.CharField(max_length=500, null=True)
    bank_account_id = models.ForeignKey('BankAccount', null=True, on_delete=models.SET_NULL)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    soft_delete     = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

class BankAccount(models.Model):
    account_number = models.IntegerField()
    bank_id        = models.ForeignKey('Bank', on_delete=models.PROTECT)
    account_holder = models.CharField(max_length=100)

    class Meta:
        db_table = 'bank_accounts'

class Bank(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'banks'


