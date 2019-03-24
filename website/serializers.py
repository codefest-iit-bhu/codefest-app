from rest_framework import serializers
from .models import *
from django.core.validators import RegexValidator

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

class ProfileSerializer(serializers.Serializer):
    institute=serializers.PrimaryKeyRelatedField(queryset=Institute.objects.all())
    study_year=serializers.IntegerField(required=False)
    degree=serializers.CharField(max_length=50,required=False)
    branch=serializers.CharField(max_length=100,required=False)
    country=serializers.CharField(max_length=100,required=True)
    phone=serializers.CharField(max_length=15,required=True)
    gender=serializers.ChoiceField(
        choices=Profile.GENDER_CHOICES,
        required=True
    )

    def validate_phone(self,number):
        phone_regex = RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )
        phone_regex(number)
        return number

    def validate_study_year(self,year):
        if year<1:
            raise serializers.ValidationError("Incorrect Year Specified")
        return year
 
    def save(self,request):
        data=self.validated_data
        profile,created=Profile.objects.get_or_create(user=request.user)
        profile.institute_name=data.get('institute')
        profile.study_year=data.get('study_year')
        profile.degree=data.get('degree')
        profile.branch=data.get('branch')
        profile.country=data.get('country')
        profile.phone=data.get('phone')
        profile.gender=data.get('gender')
        profile.is_profile_complete=True
        profile.save()
        return profile