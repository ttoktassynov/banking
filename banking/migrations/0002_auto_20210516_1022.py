# Generated by Django 3.2.3 on 2021-05-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bookingDateTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionId',
            field=models.CharField(default=0, max_length=210),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='account',
            name='identification',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='creditorIdentification',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debtorIdentification',
            field=models.CharField(max_length=256),
        ),
    ]
