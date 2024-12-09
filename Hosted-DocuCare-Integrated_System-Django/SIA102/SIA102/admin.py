from django.contrib import admin
from .models import (
    Nurse,
    PatientDischargeArchive,
    VitalSign,
    VitalSignOutput,
    InitialVital,
    IVTreatment,
    IVSideDrip,
    IVFastDrip,
    Medication,
    DeceasedDischargeArchive,
    DeceasedVitalSign,
    DeceasedVitalSignOutput,
    DeceasedInitialVital,
    DeceasedIVTreatment,
    DeceasedIVSideDrip,
    DeceasedIVFastDrip,
    DeceasedMedication,
)

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['userIdnumber', 'first_name', 'last_name', 'email']
    search_fields = ['userIdnumber', 'first_name', 'last_name', 'email']

    def save_model(self, request, obj, form, change):
        # Check if the password field has been changed
        if 'password' in form.changed_data:
            obj.set_password(obj.password)  # Hash the password before saving
        super().save_model(request, obj, form, change)

# Register other models
admin.site.register(PatientDischargeArchive)
admin.site.register(VitalSign)
admin.site.register(VitalSignOutput)
admin.site.register(InitialVital)
admin.site.register(IVTreatment)
admin.site.register(IVSideDrip)
admin.site.register(IVFastDrip)
admin.site.register(Medication)
admin.site.register(DeceasedDischargeArchive)
admin.site.register(DeceasedVitalSign)
admin.site.register(DeceasedVitalSignOutput)
admin.site.register(DeceasedInitialVital)
admin.site.register(DeceasedIVTreatment)
admin.site.register(DeceasedIVSideDrip)
admin.site.register(DeceasedIVFastDrip)
admin.site.register(DeceasedMedication)
