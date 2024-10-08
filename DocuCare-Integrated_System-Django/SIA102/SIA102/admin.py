
from django.contrib import admin
from .models import Nurse

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['userIdnumber', 'first_name', 'last_name', 'email']
    search_fields = ['userIdnumber', 'first_name', 'last_name', 'email']
