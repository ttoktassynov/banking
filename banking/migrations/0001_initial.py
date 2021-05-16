# Generated by Django 3.2.3 on 2021-05-16 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=200)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('creditDebitIndicator', models.CharField(max_length=6)),
                ('creditorIdentification', models.CharField(max_length=14)),
                ('debtorIdentification', models.CharField(max_length=14)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking.account')),
            ],
        ),
    ]
