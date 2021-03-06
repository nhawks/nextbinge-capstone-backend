# Generated by Django 3.2.8 on 2021-11-03 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_show', models.CharField(max_length=75)),
                ('username', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.comments')),
            ],
        ),
    ]
