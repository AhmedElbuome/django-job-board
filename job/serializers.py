#### get date from model ---> json

from rest_framework import routers, serializers, viewsets
from .models import job

class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = job
        
        fields = '__all__'