# Generated by Django 3.2.8 on 2021-11-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_streaming_providers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='streaming_providers',
            field=models.JSONField(default=dict),
        ),
    ]
