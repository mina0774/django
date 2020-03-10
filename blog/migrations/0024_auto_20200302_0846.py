# Generated by Django 3.0.3 on 2020-03-01 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200302_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='depth',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='groupno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='orderno',
            field=models.IntegerField(default=0),
        ),
    ]