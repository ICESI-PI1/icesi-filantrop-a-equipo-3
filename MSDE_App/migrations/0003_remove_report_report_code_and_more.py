# Generated by Django 4.2.5 on 2023-10-13 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MSDE_App', '0002_student_student_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='report_code',
        ),
        migrations.RemoveField(
            model_name='typereport',
            name='type_report_code',
        ),
        migrations.RemoveField(
            model_name='typereport',
            name='type_report_name',
        ),
        migrations.AddField(
            model_name='typereport',
            name='report_type',
            field=models.CharField(choices=[('Informe de becas', 'Informe de becas'), ('Informe de consultas en el CREA', 'Informe de consultas en el CREA'), ('Informe de actividades extra académicas', 'Informe de actividades extra académicas'), ('Informe personalizado', 'Informe personalizado')], max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='philanthropymember',
            name='philanthropy_member_email',
            field=models.CharField(default='example@gmail.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='report',
            name='philanthropy_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.philanthropymember'),
        ),
    ]
