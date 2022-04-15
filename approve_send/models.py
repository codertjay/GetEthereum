from django.db import models


class EthereumAccounts(models.Model):
    address = models.CharField(max_length=200)
    private_key = models.CharField(max_length=200)
