# Generated by Django 4.1.5 on 2023-01-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='stranger')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
