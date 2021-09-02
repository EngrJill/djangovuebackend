from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('subject-list/', views.subjectList.as_view(), name="subject-list"),
    path('subject-detail/<str:id>/', views.subjectDetail, name="subject-detail"),
    path('subject-create/', views.subjectCreate, name="subject-create"),
    path('subject-update/<str:id>/', views.subjectUpdate, name="subject-update"),
    path('subject-delete/<str:id>/', views.subjectDelete, name="task-delete"),
]

