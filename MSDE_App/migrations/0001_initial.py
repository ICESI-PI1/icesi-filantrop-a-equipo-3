# Generated by Django 4.2.5 on 2023-10-09 20:50

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
                ('collaborator_code', models.CharField(max_length=10)),
                ('collaborator_name', models.CharField(max_length=24)),
                ('collaborator_email', models.CharField(max_length=24)),
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
            name='PhilanthropyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philanthropy_member_code', models.CharField(max_length=10)),
                ('philanthropy_member_name', models.CharField(max_length=24)),
                ('philanthropy_member_email', models.CharField(default='example@gmail.com', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('Academica', 'Académica'), ('Bienestar', 'Bienestar'), ('Financiero', 'Financiero')], max_length=12, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCollaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_collaborator_code', models.CharField(max_length=10)),
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
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
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
                ('alert_code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alert_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('alert_description', models.TextField(blank=True)),
                ('alert_sender', models.CharField(blank=True, max_length=100)),
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
