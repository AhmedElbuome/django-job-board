from django.urls import path, include
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.send_message, name = 'contact'),
    path('success', views.success_page, name='success_page'),  # Add this line for the success page
]