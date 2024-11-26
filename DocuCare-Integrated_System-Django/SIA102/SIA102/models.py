from django.db import models
from django.contrib.auth.hashers import make_password

class Nurse(models.Model):
    userIdnumber = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.userIdnumber})'

class PatientDischargeArchive(models.Model):
    # Basic Patient Information
    patientID = models.IntegerField()
    name = models.CharField(max_length=255)
    patient_type = models.CharField(max_length=50)  
    age = models.IntegerField()
    sex = models.CharField(max_length=10)  
    date_of_birth = models.DateField()
    room_number = models.CharField(null=True, blank=True, max_length=50)  
    address = models.TextField(default="Address not provided")  
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField(null=True, blank=True)
    attending_physician = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)  
    discharged_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.diagnosis}"


class VitalSign(models.Model):
    # Vital signs at discharge
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="vital_signs")
    date = models.DateField()
    temperature = models.FloatField()
    pulse = models.IntegerField()
    respiration = models.IntegerField()


class VitalSignOutput(models.Model):
    # Blood pressure, urine, and stool records
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="vital_sign_outputs")
    date = models.DateField()
    blood_pressure = models.CharField(max_length=15)
    urine = models.IntegerField()
    stool = models.IntegerField()


class InitialVital(models.Model):
    # Initial vitals, e.g., weight
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="initial_vitals")
    date = models.DateTimeField()
    weight = models.CharField(max_length=20)


class IVTreatment(models.Model):
    # IV treatments
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="iv_treatments")
    date = models.DateField()
    bottle_no = models.CharField(max_length=50)
    iv_solution = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)
    incorporation = models.CharField(max_length=255)
    regulation = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.DateTimeField()
    remarks = models.TextField()


class IVSideDrip(models.Model):
    # IV side drips
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="iv_side_drips")
    date = models.DateField()
    bottle_no = models.CharField(max_length=50)
    iv_solution = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)
    incorporation = models.CharField(max_length=255)
    regulation = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.DateTimeField()
    remarks = models.TextField()


class IVFastDrip(models.Model):
    # IV fast drips
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="iv_fast_drips")
    date = models.DateField()
    ivf = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)
    incorporation = models.CharField(max_length=255)
    time_taken = models.TimeField()
    remarks = models.TextField()


class Medication(models.Model):
    # Medications
    patient = models.ForeignKey(PatientDischargeArchive, on_delete=models.CASCADE, related_name="medications")
    date = models.DateField()
    medication_name = models.CharField(max_length=255)
    medication_remarks = models.TextField()

class DeceasedDischargeArchive(models.Model):
    # Basic Patient Information
    patientID = models.IntegerField()
    name = models.CharField(max_length=255)
    patient_type = models.CharField(max_length=50)  
    age = models.IntegerField()
    sex = models.CharField(max_length=10)  
    date_of_birth = models.DateField()
    room_number = models.CharField(null=True, blank=True, max_length=50)  
    address = models.TextField(default="Address not provided")  
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField(null=True, blank=True)
    attending_physician = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)  
    discharged_by = models.CharField(max_length=255)
    cause_of_death = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.diagnosis}"


class DeceasedVitalSign(models.Model):
    # Vital signs at the time of death
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="vital_signs")
    date = models.DateField()
    temperature = models.FloatField()
    pulse = models.IntegerField()
    respiration = models.IntegerField()


class DeceasedVitalSignOutput(models.Model):
    # Blood pressure, urine, and stool records
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="vital_sign_outputs")
    date = models.DateField()
    blood_pressure = models.CharField(max_length=15)
    urine = models.IntegerField()
    stool = models.IntegerField()


class DeceasedInitialVital(models.Model):
    # Initial vitals, e.g., weight
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="initial_vitals")
    date = models.DateTimeField()
    weight = models.CharField(max_length=20)


class DeceasedIVTreatment(models.Model):
    # IV treatments
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="iv_treatments")
    date = models.DateField()
    bottle_no = models.CharField(max_length=50)
    iv_solution = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)
    incorporation = models.CharField(max_length=255)
    regulation = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.DateTimeField()
    remarks = models.TextField()


class DeceasedIVSideDrip(models.Model):
    # IV side drips
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="iv_side_drips")
    date = models.DateField()
    bottle_no = models.CharField(max_length=50)
    iv_solution = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)
    incorporation = models.CharField(max_length=255)
    regulation = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.DateTimeField()
    remarks = models.TextField()


class DeceasedIVFastDrip(models.Model):
    # IV fast drips
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="iv_fast_drips")
    date = models.DateField()
    ivf = models.CharField(max_length=255)
    volume = models.CharField(max_length=50)
    incorporation = models.CharField(max_length=255)
    time_taken = models.TimeField()
    remarks = models.TextField()


class DeceasedMedication(models.Model):
    # Medications
    patient = models.ForeignKey(DeceasedDischargeArchive, on_delete=models.CASCADE, related_name="medications")
    date = models.DateField()
    medication_name = models.CharField(max_length=255)
    medication_remarks = models.TextField()
