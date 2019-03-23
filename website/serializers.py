from rest_framework import serializers
from .models import *

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute
        fields=['name']


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventDetail
        fields=['title','content','priority']   
        ordering=['priority']    

class EventSerializer(serializers.ModelSerializer):
    details=EventDetailSerializer(source='eventdetail_set',read_only=True,many=True)
    class Meta:
        model = Event
        fields=['name','is_registration_on','min_members','max_members','details']