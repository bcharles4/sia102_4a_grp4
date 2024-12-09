# Generated by Django 5.1.1 on 2024-11-26 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SIA102", "0006_patientdischargearchive_patientid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeceasedDischargeArchive",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patientID", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("patient_type", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("sex", models.CharField(max_length=10)),
                ("date_of_birth", models.DateField()),
                ("room_number", models.CharField(blank=True, max_length=50, null=True)),
                ("address", models.TextField(default="Address not provided")),
                ("admission_date", models.DateTimeField()),
                ("discharge_date", models.DateTimeField(blank=True, null=True)),
                ("attending_physician", models.CharField(max_length=255)),
                ("diagnosis", models.CharField(max_length=255)),
                ("approved_by", models.CharField(max_length=255)),
                ("discharged_by", models.CharField(max_length=255)),
                (
                    "cause_of_death",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedInitialVital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("weight", models.CharField(max_length=20)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="initial_vitals",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedIVFastDrip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("ivf", models.CharField(max_length=255)),
                ("volume", models.CharField(max_length=50)),
                ("incorporation", models.CharField(max_length=255)),
                ("time_taken", models.TimeField()),
                ("remarks", models.TextField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="iv_fast_drips",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedIVSideDrip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("bottle_no", models.CharField(max_length=50)),
                ("iv_solution", models.CharField(max_length=255)),
                ("volume", models.CharField(max_length=50)),
                ("incorporation", models.CharField(max_length=255)),
                ("regulation", models.CharField(max_length=255)),
                ("start_time", models.TimeField()),
                ("end_time", models.DateTimeField()),
                ("remarks", models.TextField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="iv_side_drips",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedIVTreatment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("bottle_no", models.CharField(max_length=50)),
                ("iv_solution", models.CharField(max_length=255)),
                ("volume", models.CharField(max_length=50)),
                ("incorporation", models.CharField(max_length=255)),
                ("regulation", models.CharField(max_length=255)),
                ("start_time", models.TimeField()),
                ("end_time", models.DateTimeField()),
                ("remarks", models.TextField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="iv_treatments",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedMedication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("medication_name", models.CharField(max_length=255)),
                ("medication_remarks", models.TextField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medications",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedVitalSign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("temperature", models.FloatField()),
                ("pulse", models.IntegerField()),
                ("respiration", models.IntegerField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vital_signs",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeceasedVitalSignOutput",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("blood_pressure", models.CharField(max_length=15)),
                ("urine", models.IntegerField()),
                ("stool", models.IntegerField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vital_sign_outputs",
                        to="SIA102.deceaseddischargearchive",
                    ),
                ),
            ],
        ),
    ]