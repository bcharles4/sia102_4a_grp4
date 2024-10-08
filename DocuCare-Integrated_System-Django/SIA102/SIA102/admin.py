from django.contrib import admin
from .models import Nurse

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['userIdnumber', 'first_name', 'last_name', 'email']
    search_fields = ['userIdnumber', 'first_name', 'last_name', 'email']

    def save_model(self, request, obj, form, change):
        # Check if the password field has been changed
        if 'password' in form.changed_data:
            obj.set_password(obj.password)  # Hash the password before saving
        super().save_model(request, obj, form, change)
