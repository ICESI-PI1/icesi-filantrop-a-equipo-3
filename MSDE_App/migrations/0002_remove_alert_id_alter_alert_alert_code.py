# Generated by Django 4.2.5 on 2023-11-20 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSDE_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='id',
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_code',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True),
        ),
    ]