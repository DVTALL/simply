# Generated by Django 4.0.6 on 2022-08-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='images/'),
        ),
    ]
