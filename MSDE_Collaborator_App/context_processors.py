# context_processors.py

def superuser(request):
    return {
        'es_superuser': request.user.is_superuser
    }
