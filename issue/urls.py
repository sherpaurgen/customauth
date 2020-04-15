from django.contrib import admin
from django.urls import path, re_path
from .views import dashboard,issue_detail

urlpatterns = [
    path('',dashboard),
    path('issue/',issue_detail)
]
