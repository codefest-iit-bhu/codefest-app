from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.views import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.models import Token

def create_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token

# Create your views here.
class LoginView(generics.GenericAPIView):
    """
    Check the credentials and return the REST Token if the credentials are valid.
    Calls Django Auth login method to register User ID in Django session framework

    Return the Authentication Token Object's key.
    """
    authentication_classes=[]
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def get_queryset(self, *args, **kwargs):
        pass

    def login(self):
        validated_data=self.serializer.validated_data
        self.user = validated_data['user']
        self.verification_status = validated_data['is_verified']
        self.is_profile_complete = validated_data['is_profile_complete']
        self.token = create_auth_token(self.user)

    def get_response(self):
        response=LoginResponseSerializer({
            'user_id': self.user.pk,
            'token': self.token,
            'verification_status':self.verification_status,
            'is_profile_complete':self.is_profile_complete,
        })
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class RegisterView(generics.GenericAPIView):
    authentication_classes=[]
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer

    def get_queryset(self, *args, **kwargs):
        pass

    def register(self):
        self.user = self.serializer.save()
        self.token = create_auth_token(self.user)

    def get_response(self):
        response= RegisterResponseSerializer({
            'user_id':self.user.pk,
            'token':self.token,
            'verification_status':self.user.verified_account.is_verified,
        })
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        self.request=request
        self.serializer = self.get_serializer(
            data=request.data , context={'request': request}
        )
        self.serializer.is_valid(raise_exception=True)
        self.register()
        return self.get_response()
        