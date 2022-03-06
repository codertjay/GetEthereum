from django.db import models


class EthereumAccounts(models.Model):
    to_account = models.CharField(max_length=200)
    from_account = models.CharField(max_length=200)
    private_key = models.CharField(max_length=200)
    eth_type = models.CharField(max_length=50)
