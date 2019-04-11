from rest_framework import serializers
from .models import *
from django.core.validators import RegexValidator
from drf_yasg.utils import swagger_serializer_method


# class EventDetailSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model=EventDetail
#         fields=['title','content','priority']   
#         ordering=['priority']    


class ProfileSerializer(serializers.Serializer):
    institute=serializers.CharField(max_length=128, required=True)
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
        profile.get_or_set_profile_status(toSet=True)
        profile.save()
        return profile

class TeamCreationSerializer(serializers.Serializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    team_name = serializers.CharField()

    def validate(self, attrs):
        name = attrs['team_name']
        if len(name)<2:
            raise serializers.ValidationError("Team name must be of atleast 2 characters")
        event = attrs['event']
        user =  self.context['request'].user
        if Team.objects.filter(name=name, event=event).count()!=0:
            raise serializers.ValidationError("Team name unavailable")
        
        if Membership.objects.filter(team__event=event, profile=user.profile).count()!=0:
            raise serializers.ValidationError("You cannot be part of more than one team for the same event")
            
        return_dict={}
        return_dict['team_name']=name
        return_dict['event']=event
        return_dict['user'] = user
        return return_dict

    def  save(self):
        data = self.validated_data
        team_name=data['team_name']
        event = data['event']
        user = data['user']
        return event.create_team(user.profile, team_name)

class TeamJoinSerializer(serializers.Serializer):
    access_code = serializers.CharField()

    def validate(self, data):
        access_code=data['access_code']
        user =  self.context['request'].user
        if Team.objects.filter(access_code=access_code).count()==0:
            raise serializers.ValidationError("Invalid Access Code")

        team = Team.objects.get(access_code=access_code)
        event =team.event
        if Membership.objects.filter(team__event=event, profile=user.profile).count()!=0:
            raise serializers.ValidationError("You cannot be part of more than one team for the same event")

        return_dict ={}
        return_dict['team']=team
        return_dict['user'] = user
        return_dict['access_code']=access_code
        return return_dict
    def save(self):
        data = self.validated_data
        user = data['user']
        access_code = data['access_code']
        team=data['team']
        team.join_team(user.profile, access_code)
        return team


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields=('id', 'name')

class TeamDetailSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    
    class Meta:
        model =Team
        fields='__all__'


class EventSerializer(serializers.ModelSerializer):
    # details=EventDetailSerializer(source='eventdetail_set',read_only=True,many=True)
    team = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields=['name','slug', 'is_registration_on','min_members','max_members','team']

    @swagger_serializer_method(serializer_or_field=TeamDetailSerializer)
    def get_team(self, obj):
        profile = self.context['request'].user.profile
        try:
            team = profile.team_members.get(event = obj)
        except:
            return None
        return TeamDetailSerializer(team).data