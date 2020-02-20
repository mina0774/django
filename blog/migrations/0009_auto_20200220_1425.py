# Generated by Django 3.0.3 on 2020-02-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200220_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent_title',
            field=models.CharField(choices=[('Profile', (('ProfileSkill', 'Skill'),)), ('Activity', (('UCI Undergraduate Researcher', 'UCI Undergraduate Researcher'), ('Coding HelpDesk', 'Coding HelpDesk'), ('Heronation InternShip', 'Heronation InternShip'))), ('Project', (('Face Recogntion', 'Face Recognition'), ('Mu:Ping App', 'Mu:Ping App'), ('Ang-Bob App', 'Ang-Bob App'), ('Flex-Bison Interpreter', 'Flex-Bison Interpreter'), ('Z-shop App', 'Z-shop App')))], default='Skill', max_length=30),
        ),
    ]