from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,generics,mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import TeamSerializer,InstituteSerializer,RegistrationSerializer
from .models import *
# Create your views here.

class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class InstituteListView(generics.ListAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class=InstituteSerializer
    queryset=Institute.objects.all()

class TeamView(generics.ListCreateAPIView):
    # authentication_classes=[]
    # permission_classes=[]
    serializer_class=TeamSerializer
    
    def get_queryset(self):
        user = self.request.user
        return user.profile.team_members.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

class InvitationListView(generics.GenericAPIView,mixins.ListModelMixin,mixins.DestroyModelMixin):
    serializer_class=InvitationSerializer

    def get_queryset(self):
        user=self.request.user
        return user.profile.received_invitations.all()

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def perform_destory(self,instance):
        
        instance.delete()
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

class RegistrationView(generics.CreateAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class=RegistrationSerializer