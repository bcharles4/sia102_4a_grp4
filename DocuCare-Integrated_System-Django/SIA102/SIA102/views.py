from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests


def login_view(request):
    if request.method == "POST":

        username = request.POST["userID"]
        password = request.POST["uPassword"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "SIA102/index.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "SIA102/index.html")

def logout_view(request):
    logout(request)
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