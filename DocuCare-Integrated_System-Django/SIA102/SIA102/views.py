from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.hashers import check_password
from .models import Nurse
from django.http import JsonResponse

ngrok = "https://2408-136-158-67-130.ngrok-free.app"

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


def index(request):
    return render(request, "SIA102/index.html")

def get_users_data(request):
    try:
        # Make a request to your DocuCare API endpoint
        response = requests.get(f'{ngrok}/DocuCare/get_users.php')

        # Check if the request was successful
        if response.status_code == 200:
            users_data = response.json()  # Parse the response as JSON
        else:
            users_data = []  # If API request fails, return an empty list
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        users_data = []  # If there’s an error with the API request, return an empty list

    # Return the users data as a JSON response
    return JsonResponse({'users': users_data})

def users(request):
    return render(request, 'SIA102/users.html')

def dashboard(request):
    return render(request, "SIA102/dashboard.html")

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