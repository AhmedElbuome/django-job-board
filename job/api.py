#### views

from .models import job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework import generics

@api_view(['GET'])
def Job_List_api(request):
    
    all_job = job.objects.all()
    data =JobSerializer(all_job, many= True).data
    
    return Response({'data': data})

@api_view(['GET'])
def Job_Detail_api(request, id):
    
    job_detail = job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})

class Job_List_Api(generics.ListAPIView):
    
    queryset = job.objects.all()
    serializer_class = JobSerializer
    
class Job_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'