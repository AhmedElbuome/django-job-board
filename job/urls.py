from django.urls import path, include
from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name = 'job_list'),
    path('add', views.add_job, name = 'add_job'),
    path('<str:slug>', views.job_detail, name = 'job_detail'),
    
    # api
    path('api/jobs', api.Job_List_api, name = 'Job_List_api'),
    path('api/jobs/<int:id>', api.Job_Detail_api, name = 'Job_Detail_api'),
    
    # api v2
    path('api/v2/jobs', api.Job_List_Api.as_view(), name = 'Job_List_Api'),
    path('api/v2/jobs/<int:id>', api.Job_Detail_Api.as_view(), name = 'Job_Detail_api'),
    
]