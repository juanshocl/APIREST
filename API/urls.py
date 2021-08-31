from pathlib import Path
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from API import views

urlpatterns = [
    path('persona/',views.PersonaList.as_view(), name='persona_list'),
]