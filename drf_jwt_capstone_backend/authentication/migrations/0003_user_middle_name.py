# Generated by Django 3.2.8 on 2021-11-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(default='john', max_length=20),
            preserve_default=False,
        ),
    ]
