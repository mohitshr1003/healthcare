from django.contrib import admin

from reception.models import *

# Register your models here.
admin.site.register(PatientDetail)
admin.site.register(DoctorDetail)
admin.site.register(UserRole)
admin.site.register(DepartmentDetail)