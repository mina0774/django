# Generated by Django 3.0.3 on 2020-02-27 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_menu_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='menu',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='blog.Menu'),
            preserve_default=False,
        ),
    ]
