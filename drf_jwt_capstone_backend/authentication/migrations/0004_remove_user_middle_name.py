# Generated by Django 3.2.8 on 2021-11-03 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_middle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
    ]
