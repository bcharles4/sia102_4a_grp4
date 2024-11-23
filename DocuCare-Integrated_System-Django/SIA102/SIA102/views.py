from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.hashers import check_password
from .models import Nurse
from django.http import JsonResponse
from collections import Counter

from collections import defaultdict
from datetime import datetime

ngrok = "https://4f19-136-158-66-138.ngrok-free.app/docu_care-copy-main"

def login_view(request):
    if request.method == "POST":
        userIdnumber = request.POST["userID"]
        password = request.POST["uPassword"]

        try:
            nurse = Nurse.objects.get(userIdnumber=userIdnumber)
            print("Nurse found")
            if check_password(password, nurse.password):
                request.session['userID'] = nurse.userIdnumber
                request.session['fullname'] = f"{nurse.first_name} {nurse.last_name}"
                print("Storing session ID")
                return HttpResponseRedirect(reverse("dashboard"))
            else:
                print("Invalid UserID and/or password.")
                return render(request, "SIA102/index.html")
        except Nurse.DoesNotExist:
            print("Nurse does not exist")
            return render(request, "SIA102/index.html")
    else:
        print("GET request received")
        return render(request, "SIA102/index.html")


def logout_view(request):
    if 'userID' in request.session:
        del request.session['userID']
    return HttpResponseRedirect(reverse("index"))

def get_illness_data(request):
    try:
        # Use the existing API to get all patient information
        response = requests.get(f'{ngrok}/DocuCare/get_patientsInfo.php')
        
        if response.status_code == 200:
            patients_info = response.json()  # Retrieve the list of patients
            
            # Extract all 'Admitting_Diagnosis' entries
            diagnoses = [patient['Admitting_Diagnosis'] for patient in patients_info if 'Admitting_Diagnosis' in patient]
            
            # Count occurrences of each illness
            diagnosis_counts = Counter(diagnoses)

            # Prepare data for the chart
            labels = list(diagnosis_counts.keys())
            data = list(diagnosis_counts.values())
            
            return JsonResponse({'illness_data': {'labels': labels, 'data': data}})
        else:
            return JsonResponse({'error': 'Failed to fetch data from external API'}, status=500)
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return JsonResponse({'error': 'API request failed'}, status=500)

def monthly_illness_distribution(request):
    try:
        response = requests.get(f'{ngrok}/DocuCare/get_patientsInfo.php')
        if response.status_code == 200:
            patients_info = response.json()
            
            # Initialize a structure to hold monthly counts per illness
            monthly_data = defaultdict(lambda: defaultdict(int))
            all_years = set()  # Track all years in the dataset
            
            for patient in patients_info:
                diagnosis = patient.get('Admitting_Diagnosis', 'Unknown')
                admission_date = patient.get('Admission_Date')
                if admission_date:
                    # Parse the admission date
                    date_obj = datetime.strptime(admission_date, '%Y-%m-%d %H:%M:%S')
                    year_month = (date_obj.year, date_obj.month)
                    monthly_data[diagnosis][year_month] += 1
                    all_years.add(date_obj.year)  # Add year to the set of years
            
            # Format the data for the chart
            formatted_data = {}
            for diagnosis, counts in monthly_data.items():
                yearly_data = defaultdict(lambda: [0] * 12)
                for (year, month), count in counts.items():
                    yearly_data[year][month - 1] = count

                # Make sure every year in all_years is included for this illness
                for year in all_years:
                    if year not in yearly_data:
                        yearly_data[year] = [0] * 12

                formatted_data[diagnosis] = yearly_data

        else:
            formatted_data = {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        formatted_data = {}

    return JsonResponse(formatted_data)

def illness_deaths_data(request):
    try:
        response = requests.get(f'{ngrok}/DocuCare/get_patientsInfo.php')
        if response.status_code == 200:
            patients_info = response.json()
            # Filter for deceased patients
            deceased_patients = [p for p in patients_info if p.get('Status') == "DEC"]

            # Categorize by Admitting_Diagnosis
            diagnosis_count = {}
            for patient in deceased_patients:
                diagnosis = patient.get('Admitting_Diagnosis', 'Unknown')
                diagnosis_count[diagnosis] = diagnosis_count.get(diagnosis, 0) + 1
        else:
            diagnosis_count = {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        diagnosis_count = {}

    # Return the data in JSON format
    return JsonResponse(diagnosis_count)

def mortality_data_by_month_and_year(request):
    try:
        response = requests.get(f'{ngrok}/DocuCare/get_patientsInfo.php')
        if response.status_code == 200:
            patients_info = response.json()
            
            # Filter for deceased patients
            deceased_patients = [p for p in patients_info if p.get('Status') == "DEC"]
            
            # Categorize deaths by month and year
            mortality_data = {}
            for patient in deceased_patients:
                death_date = patient.get('Admission_Date')  # Assuming discharge date is when death is recorded
                if death_date:
                    date_obj = datetime.strptime(death_date, '%Y-%m-%d %H:%M:%S')
                    year = date_obj.year
                    month = date_obj.month - 1  # Zero-based for JavaScript compatibility
                    
                    if year not in mortality_data:
                        mortality_data[year] = [0] * 12
                    mortality_data[year][month] += 1
        else:
            mortality_data = {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        mortality_data = {}

    # Return the data in JSON format
    return JsonResponse(mortality_data)

def index(request):
    return render(request, "SIA102/index.html")

def users(request):
    return render(request, 'SIA102/users.html')

def dashboard(request):
    # Fetch patients info
    try:
        patients_response = requests.get(f'{ngrok}/DocuCare/get_patientsInfo.php')
        if patients_response.status_code == 200:
            patients_info = patients_response.json()
            # Count patients with "ALV" status
            alive_patients_count = sum(1 for patient in patients_info if patient.get('Status') == "ALV")
        else:
            alive_patients_count = 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        alive_patients_count = 0

    # Fetch rooms info
    try:
        rooms_response = requests.get(f'{ngrok}/DocuCare/get_roomsInfo.php')
        if rooms_response.status_code == 200:
            rooms_info = rooms_response.json()
            # Count total rooms
            total_rooms = len(rooms_info)
        else:
            total_rooms = 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        total_rooms = 0

    # Pass data to the template
    context = {
        'patientsAdmitted': alive_patients_count,
        'roomsOccupied': total_rooms,
    }
    return render(request, 'SIA102/dashboard.html', context)

def dischargeRecords(request):
    return render(request, "SIA102/dischargeRecords.html")

def get_patients_info(request):
    try:
        response = requests.get(f'{ngrok}/DocuCare/get_patientsInfo.php')
        if response.status_code == 200:
            patients_info = response.json()  
        else:
            patients_info = []  
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        patients_info = [] 

    return JsonResponse({'patients': patients_info})

def patientList(request):
    return render(request, "SIA102/patientList.html")

def get_rooms_info(request):
    try:
        response = requests.get(f'{ngrok}/DocuCare/get_roomsInfo.php')
        if response.status_code == 200:
            rooms_info = response.json()  
        else:
            rooms_info = []  
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        rooms_info = [] 

    return JsonResponse({'rooms': rooms_info})

def roomStatus(request):
    return render(request, "SIA102/roomStatus.html")

def dischargeSummary(request, userName):
    return render(request, "SIA102/dischargeSummary.html",
    {
        "patientName": userName
    })

def patient_detail(request, patient_id):
    try:
        # Make an API call to get the specific patient's details
        response = requests.get(
            f'{ngrok}/DocuCare/get_specific_patient.php',
            params={'patient_id': patient_id}
        )
        if response.status_code == 200:
            patient_info = response.json()
        else:
            patient_info = None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        patient_info = None

    # Pass the patient's data to the template
    return render(request, 'SIA102/patientDetail.html', {
        'patient': patient_info[0] if patient_info else {},
    })


def notifications(request):
    return render(request, "SIA102/notifications.html")

def get_dischargeInfo(request, patient_id):
    try:
        response1 = requests.get(
            f'{ngrok}/DocuCare/getDischargeInfo.php',
            params={'patient_id': patient_id}
        )
        if response1.status_code == 200:
            patient_dischargeInfo = response1.json()
        else:
            patient_dischargeInfo = []

        response2 = requests.get(
            f'{ngrok}/DocuCare/get_patientVitals.php',
            params={'patient_id': patient_id}
        )
        if response2.status_code == 200:
            patient_vitals = response2.json()
        else:
            patient_vitals = []

        response3 = requests.get(
            f'{ngrok}/DocuCare/get_specific_patient.php',
            params={'patient_id': patient_id}
        )
        if response3.status_code == 200:
            patient_info = response3.json()
        else:
            patient_info = None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        patient_dischargeInfo = []
        patient_vitals = []
        patient_info = None
        

    return render(request, 'SIA102/dischargeSummary.html', 
    {
        'patientInfo': patient_info[0],
        'dischargeInfo': patient_dischargeInfo,
        'vitals': patient_vitals,
    })