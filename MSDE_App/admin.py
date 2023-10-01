from django.contrib import admin
from .models import Student, Donor, Alert, TypeAlert
# Register your models here.

admin.site.register(Student)
admin.site.register(Donor)
admin.site.register(Alert)
admin.site.register(TypeAlert)
