# Generated by Django 4.2.4 on 2023-09-10 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_app', '0011_contact_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=220)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.TimeField(default=datetime.time(18, 2, 22, 815534)),
        ),
    ]
