from django.contrib import admin
from .models import Student, Donor, Alert, TypeAlert, User
# Register your models here.

admin.site.register(Student)
admin.site.register(Donor)
admin.site.register(Alert)
admin.site.register(TypeAlert)
admin.site.register(User)
