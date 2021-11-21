# Generated by Django 3.2.9 on 2021-11-15 23:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateBooked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2021, 11, 15, 20, 22, 57, 478093))),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.court')),
            ],
        ),
    ]
