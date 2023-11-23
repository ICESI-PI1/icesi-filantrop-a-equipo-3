from django.apps import AppConfig

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command


@receiver(post_migrate)
def initial_data(sender, **kwargs):
    if sender.name == 'MSDE_App':  # Reemplaza 'miapp' con el nombre de tu aplicación
        call_command('loaddata', 'initial_data.json', app='MSDE_App')

class MsdeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MSDE_App'
