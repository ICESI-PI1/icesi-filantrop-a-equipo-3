# Generated by Django 4.2.5 on 2023-11-20 06:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaborator_code', models.CharField(max_length=10, unique=True)),
                ('collaborator_name', models.CharField(max_length=24)),
                ('collaborator_email', models.CharField(max_length=24)),
                ('collaborator_type', models.CharField(choices=[('Bienestar Universitario', 'Bienestar Universitario'), ('Registro Académico', 'Registro Académico'), ('Director de Programa', 'Director de Programa'), ('Apoyo Financiero', 'Apoyo Financiero')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_code', models.CharField(max_length=12, unique=True)),
                ('donor_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_from', models.CharField(max_length=12)),
                ('message_to', models.CharField(max_length=12)),
                ('message_content', models.CharField(max_length=3000)),
                ('message_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PhilanthropyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philanthropy_member_code', models.CharField(max_length=10, unique=True)),
                ('philanthropy_member_name', models.CharField(max_length=24)),
                ('philanthropy_member_email', models.CharField(default='example@gmail.com', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('Académica', 'Académica'), ('Bienestar', 'Bienestar'), ('Financiero', 'Financiero')], max_length=12, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCollaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_collaborator_code', models.CharField(max_length=10, unique=True)),
                ('type_collaborator_name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='TypeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('Informe de becas', 'Informe de becas'), ('Informe de consultas en el CREA', 'Informe de consultas en el CREA'), ('Informe de actividades extra académicas', 'Informe de actividades extra académicas'), ('Informe personalizado', 'Informe personalizado')], max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('user_type', models.CharField(max_length=150)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('date_joined', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(max_length=9, unique=True)),
                ('student_name', models.CharField(max_length=24)),
                ('student_surname', models.CharField(max_length=24, null=True)),
                ('student_birth_date', models.DateField(max_length=10)),
                ('student_id', models.CharField(max_length=10)),
                ('student_email', models.CharField(max_length=50)),
                ('student_phone_number', models.CharField(max_length=12)),
                ('student_ICFES_score', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='student_pictures/')),
                ('donor_student_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.donor')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(max_length=10)),
                ('philanthropy_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.philanthropymember')),
                ('student_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.student')),
                ('type_report_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.typereport')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraAcademic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_academic_name', models.CharField(max_length=100)),
                ('extra_academic_hours', models.IntegerField()),
                ('student_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.student')),
            ],
        ),
        migrations.CreateModel(
            name='CreaQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crea_query_date', models.DateField()),
                ('crea_query_info', models.CharField(max_length=500)),
                ('student_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.student')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_code', models.CharField(max_length=9, unique=True)),
                ('alert_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('alert_description', models.TextField(blank=True)),
                ('alert_sender', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.student')),
                ('type_alert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.typealert')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_balance_career', models.CharField(max_length=50)),
                ('academic_balance_subjects', models.CharField(max_length=50)),
                ('academic_balance_schedule', models.CharField(max_length=50)),
                ('academic_balance_additions', models.CharField(max_length=50)),
                ('academic_balance_cancellations', models.CharField(max_length=50)),
                ('academic_balance_semester_average', models.FloatField()),
                ('academic_balance_total_average', models.FloatField()),
                ('student_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MSDE_App.student')),
            ],
        ),
    ]
