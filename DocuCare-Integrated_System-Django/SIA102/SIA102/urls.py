"""
URL configuration for SIA102 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("notifications/", views.notifications, name="notifications"),
    path('get_illness_data/', views.get_illness_data, name='get_illness_data'),
    path('monthly_illness_distribution/', views.monthly_illness_distribution, name='monthly_illness_distribution'),
    path('illness_deaths_data/', views.illness_deaths_data, name='illness_deaths_data'),
    path('mortality_data/', views.mortality_data_by_month_and_year, name='mortality_data'),
    path("dischargeRecords/", views.dischargeRecords, name="dischargeRecords"),
    path("patientList/", views.patientList, name="patientList"),
    path('patient/<str:patient_id>', views.patient_detail, name='patient'),
    path("roomStatus/", views.roomStatus, name="roomStatus"),
    path('get_rooms_info/', views.get_rooms_info, name='get_rooms_info'),
    path('get_patients_info/', views.get_patients_info, name='get_patients_info'),
    path('discharge/<int:patient_id>/<str:createdAt>/<int:doctor_id>/', views.get_dischargeInfo, name='discharge'),
    path('dischargeSummary/<int:patient_id>/', views.dischargeSummary, name='dischargeSummary')
]
