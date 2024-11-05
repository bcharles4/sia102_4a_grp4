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
    path("dischargeRecords/", views.dischargeRecords, name="dischargeRecords"),
    path("patientList/", views.patientList, name="patientList"),
    path('patient/<str:patient_id>', views.patient_detail, name='patient'),
    path("roomStatus/", views.roomStatus, name="roomStatus"),
    path('users/', views.users, name='users'),
    path('get_users_data/', views.get_users_data, name='get_users_data'),
    path('dischargeSummary/<str:userName>/', views.dischargeSummary, name='dischargeSummary')
]
