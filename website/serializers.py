from rest_framework import serializers
from .models import *
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields=['name','event','all_members','creator','is_active']

class InvitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TeamInvitation
        fields=['leader','team','to','event']

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute

class RegistrationSerialzer(serializers.)