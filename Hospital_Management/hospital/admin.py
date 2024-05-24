from django.contrib import admin
from .models import Doctors,Patient,Ward,Patient_History


#Doctor
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ("id","name","speciality","fees")
#Doctor
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id","pname","mobile","address","issue","emergency_visit")
class PatientHistoryAdmin(admin.ModelAdmin):
    list_display = ("pid","pname","hname","doctor")

# Register your models here.
admin.site.register(Doctors,DoctorsAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Patient_History,PatientHistoryAdmin)
admin.site.register(Ward)