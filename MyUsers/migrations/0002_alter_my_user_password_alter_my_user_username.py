# Generated by Django 5.1.1 on 2024-10-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='password',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='my_user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
