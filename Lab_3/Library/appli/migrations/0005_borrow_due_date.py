# Generated by Django 4.1.5 on 2023-02-01 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0004_borrow_book_borrow_cust_alter_borrow_is_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
