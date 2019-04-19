from rest_framework import serializers
from .utils import FirebaseAPI
from .models import *
from website.models import Profile,ValidReferral
from django.conf import settings
from rest_framework.exceptions import ParseError
import requests
class LoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(max_length=2400)
    provider_token = serializers.CharField(max_length=2400, required=False)

    def validate_access_token(self, access_token):
        return FirebaseAPI.verify_id_token(access_token)

    def validate(self, attrs):
        id_token = attrs.get('id_token', None)
        provider_token = attrs.get('provider_token', None)

        user = None

        if id_token:
            jwt = self.validate_access_token(id_token)
            uid = jwt['uid']
            provider=FirebaseAPI.get_provider(jwt)
            
            try:
                account = VerifiedAccount.objects.get(pk=uid)
            except VerifiedAccount.DoesNotExist:
                raise serializers.ValidationError('No such account exists')
            
            user = account.user
            # add the verification status to the validated data 
            attrs['is_verified']=account.get_verified_status()   
            profile=user.profile
            # because we also need the frontend to know if the profile is complete
            # this line automatically applies referral code if needed
            attrs['is_profile_complete']=profile.get_or_set_profile_status()
            if provider_token:
                account.provider_token = provider_token
                account.save()
        else:
            raise ParseError('Provide access_token or username to continue.')
        # Did we get back an active user?
        if user:
            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')
        else:
            raise serializers.ValidationError(
                'Unable to log in with provided credentials.')

        attrs['user'] = user
        return attrs


class RegisterSerializer(serializers.Serializer):
    
    id_token = serializers.CharField(max_length=2400, required=True)
    # provider_token = serializers.CharField(max_length=2400, required=False)
    first_name = serializers.CharField(max_length=40, allow_blank=False)
    last_name = serializers.CharField(max_length=100, allow_blank=True, required=False)
    applied_referral_code = serializers.CharField(max_length=500,required=False, allow_blank=True)
    # g_recaptcha_response = serializers.CharField(max_length=500, required=True)

    def validate_id_token(self, access_token):
        return FirebaseAPI.verify_id_token(access_token)

    def validate_first_name(self,name):
        if name==None or name=='':
            raise serializers.ValidationError("First Name cannot be blank")
        return name

    def validate_applied_referral_code(self,code):
        if code is None or code=="":
            return None
        try:
            referred_by=Profile.objects.get(referral_code=code)
            if not referred_by.get_or_set_profile_status():
                raise serializers.ValidationError("Invalid Referral Code")
        except:
            raise serializers.ValidationError("Invalid Referral Code")
        return referred_by
        
    # def validate_g_recaptcha_response(self, token):
    #     data= {
    #         'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
    #         'response':token
    #     }
    #     response = requests.post(settings.GOOGLE_RECAPTCHA_URL, data = data)
    #     response = response.json()
    #     if response['success'] and response['score']>=0.5:
    #         return
    #     raise serializers.ValidationError("Captcha could not be verified. Please try again.")

    def get_user(self, data,uid):
        user = User()
        user.username = uid
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name',"")
        user.gender = data.get('gender')
        return user

    
    def save(self):
        data = self.validated_data
        jwt = data.get('id_token')
        # print(jwt)
        uid = jwt['uid']
        provider = FirebaseAPI.get_provider(jwt)
        # provider_uid = None
        # if provider !=VerifiedAccount.AUTH_EMAIL_PROVIDER:
        #     provider_uid = FirebaseAPI.get_provider_uid(jwt, provider)
        user = self.get_user(data,uid)
        try:
            user.validate_unique()
        except Exception as e:
            raise serializers.ValidationError(detail=e.message_dict)
        user.save()
        account, _ = VerifiedAccount.objects.get_or_create(
            uid=uid, user=user, provider=provider)

        if provider == VerifiedAccount.AUTH_EMAIL_PROVIDER:
            account.is_verified=False
            account.save()
        
        try:
            referred_by = Profile.objects.get(referral_code = data.get('applied_referral_code'))
        except:
            referred_by = None
        profile,_ = Profile.objects.get_or_create(user=user,referred_by=referred_by)
        profile.save()
        return user


class RegisterResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    token = serializers.CharField(max_length = 500)
    verification_status = serializers.BooleanField()



class LoginResponseSerializer(serializers.Serializer):
    user_id= serializers.IntegerField()
    token = serializers.CharField(max_length=500)
    verification_status = serializers.BooleanField()
    is_profile_complete = serializers.BooleanField()