from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.hashers import check_password
from .models import Nurse

def login_view(request):
    if request.method == "POST":
        userIdnumber = request.POST["userID"]
        password = request.POST["uPassword"]

        try:
            nurse = Nurse.objects.get(userIdnumber=userIdnumber)
            print("Nurse found")
            if check_password(password, nurse.password):
                request.session['nurse_userID'] = nurse.userIdnumber
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
    if 'nurse_id' in request.session:
        del request.session['nurse_id']
    return HttpResponseRedirect(reverse("index"))


def index(request):
    return render(request, "SIA102/index.html")

# Define a view to fetch and display users from the DocuCare API
def users(request):
    try:
        # Make a request to your DocuCare API endpoint
        response = requests.get('https://01bd-136-158-66-67.ngrok-free.app/DocuCare/get_users.php')
        # Check if the request was successful
        if response.status_code == 200:
            users_data = response.json()
        else:
            users_data = []
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the API request
        print(f"An error occurred: {e}")
        users_data = []

    # Render the users.html template, passing the users_data to it
    return render(request, 'SIA102/users.html', {
        'users': users_data
    })

def dashboard(request):
    return render(request, "SIA102/dashboard.html")

def dischargeRecords(request):
    return render(request, "SIA102/dischargeRecords.html")

def patientList(request):
    return render(request, "SIA102/patientList.html")

def roomStatus(request):
    return render(request, "SIA102/roomStatus.html")

def dischargeSummary(request, userName):
    return render(request, "SIA102/dischargeSummary.html",
    {
        "patientName": userName
    })

def patient_detail(request, patient_id):
    return render(request, "SIA102/patientDetail.html",
    {
        "patientID": patient_id
    })