"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from club_admin import views
from django.urls import path,include,re_path

urlpatterns = [
    path('',views.index,name="index"),
    path('adminlogin/',views.adminlog,name="adminlogin"),
    re_path('admin/',views.admin,name="admin"),
    path('super_admin/',views.super_admin,name="super_admin"),
    path('delete/', views.delete_session,name="delete_session"),
    path('addadmin/',views.addadmin,name="addadmin")
]
