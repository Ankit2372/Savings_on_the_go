# Generated by Django 3.1.2 on 2020-10-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addmoney_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_money', models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], max_length=10)),
                ('quantity', models.BigIntegerField()),
                ('Category', models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], default='Food', max_length=20)),
            ],
        ),
    ]