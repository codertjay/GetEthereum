# Generated by Django 3.2.12 on 2022-03-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fetch_api', '0006_delete_placeholder'),
    ]

    operations = [
        migrations.CreateModel(
            name='EthereumAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_account', models.CharField(max_length=200)),
                ('from_account', models.CharField(max_length=200)),
                ('private_key', models.CharField(max_length=200)),
            ],
        ),
    ]