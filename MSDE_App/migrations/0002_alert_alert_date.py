# Generated by Django 4.2.5 on 2023-10-02 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MSDE_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='alert_date',
            field=models.DateField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
