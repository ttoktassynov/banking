# Generated by Django 3.2.3 on 2021-05-16 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_auto_20210516_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transactionId',
        ),
    ]