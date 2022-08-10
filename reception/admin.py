from django.contrib import admin

from reception.models import *

# Register your models here.
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(UserRole)