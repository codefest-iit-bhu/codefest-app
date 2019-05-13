from rest_framework import serializers
from .models import *
from django.core.validators import RegexValidator
from drf_yasg.utils import swagger_serializer_method

phone_regex = RegexValidator(
    regex=r'^\+\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=128, read_only=True, required=False)
    institute_name=serializers.CharField(max_length=128, required=True)
    study_year=serializers.IntegerField(required=True)
    degree=serializers.CharField(max_length=50,required=False, allow_blank=True, default="", allow_null=True)
    branch=serializers.CharField(max_length=100,required=False, allow_blank=True, default="", allow_null=True)
    country=serializers.CharField(max_length=100,required=True)
    phone=serializers.CharField(max_length=15,required=True, validators=[phone_regex,])
    institute_type = serializers.ChoiceField(
        choices=Profile.INSTITUTE_TYPE_CHOICES,
        required=True
    )
    gender=serializers.ChoiceField(
        choices=Profile.GENDER_CHOICES,
        required=True
    )
    is_profile_complete = serializers.SerializerMethodField()
    is_verified = serializers.SerializerMethodField()
    referral_code = serializers.CharField(max_length=200,read_only=True)
    provider = serializers.SerializerMethodField()
    referral_count = serializers.IntegerField(read_only = True)

    class Meta:
        model = Profile
        fields = ('id','name','institute_name', 'study_year', 'degree', 'branch',
             'country', 'institute_type', 'phone', 'gender',
             'is_profile_complete', 'referral_code','referral_count','provider','is_verified')

    @swagger_serializer_method(serializer_or_field=serializers.CharField)
    def get_provider(self, obj):
        return obj.user.verified_account.provider

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_verified(self, obj):
        return obj.user.verified_account.get_verified_status()
    
    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_is_profile_complete(self, obj):
        return obj.get_or_set_profile_status()

    def validate_country(self, country):
        if len(country)>4:
            raise serializers.ValidationError("Country Code of upto 4 characters allowed.")
        return country
    
    def validate_study_year(self,year):
        if year<1:
            raise serializers.ValidationError("Incorrect Year Specified")
        return year

    def update(self, instance, data):
        instance.get_or_set_profile_status(toSet=True)
        return super().update(instance, data)

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
    creator = serializers.SerializerMethodField()

    class Meta:
        model =Team
        fields='__all__'

    @swagger_serializer_method(serializer_or_field=serializers.BooleanField)
    def get_creator(self, obj):
        profile = self.context['request'].user.profile
        if obj.creator == profile:
            return True
        else:
            return False

class RemoveFromTeamSerializer(serializers.Serializer):
    member = serializers.PrimaryKeyRelatedField(queryset = Profile.objects.all(), required=True)

    def validate(self, attrs):
        user_profile = self.context['request'].user.profile
        team = self.context['team']
        member = attrs['member']
        return_dict={}
        return_dict['team']=team
        return_dict['member'] = member
        if not team.creator == user_profile:
            raise serializers.ValidationError("User not creator of requested team")
        if team.creator == member:
            raise serializers.ValidationError("Team creator cannot remove self from team. Use team leave option instead.") 
        if Membership.objects.filter(team=team, profile=member).count()==0:
            raise serializers.ValidationError("Requested user to remove not a part of requested team.")
        return return_dict
    
    def delete(self):
        data = self.validated_data
        team = data['team']
        team.leave_team(data['member'])
        return team    

class EventSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields=['id','name','slug', 'is_registration_on','min_members','max_members','team']

    @swagger_serializer_method(serializer_or_field=TeamDetailSerializer)
    def get_team(self, obj):
        profile = self.context['request'].user.profile
        try:
            team = profile.team_members.get(event = obj)
        except:
            return None
        return TeamDetailSerializer(team, context=self.context).data

class HandleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Handles
        exclude = ('id','profile')

class LeaderBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('name','institute_name','referral_count')

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Profile
        fields=('resume',)

class CALeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=CA
        fields = '__all__'