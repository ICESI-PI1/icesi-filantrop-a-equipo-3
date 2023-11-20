from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSDE_App', '0002_alert_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_from', models.CharField(max_length=12)),
                ('message_to', models.CharField(max_length=12)),
                ('message_content', models.CharField(max_length=3000)),
                ('message_date', models.DateField(auto_now_add=True, null=True)),

            ],
        ),
    ]
