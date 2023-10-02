# Generated by Django 4.2.5 on 2023-10-01 19:03

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MSDE_App', '0005_remove_typealert_type_alert_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='id',
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='alert_sender',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
