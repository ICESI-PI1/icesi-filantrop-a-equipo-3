# Generated by Django 4.2.5 on 2023-09-20 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MSDE_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='donor_student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.donor'),
            preserve_default=False,
        ),
    ]
