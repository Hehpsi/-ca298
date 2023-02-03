# Generated by Django 4.1.5 on 2023-01-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('author', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('title', models.TextField()),
                ('synopsis', models.TextField()),
                ('category', models.TextField(default='Action')),
            ],
        ),
    ]