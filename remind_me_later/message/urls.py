from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_reminder, name='create_reminder'),
    path('created/', views.reminder_created, name='reminder_created'),
]
