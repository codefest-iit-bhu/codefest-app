from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
import hashlib
from hashids import Hashids
hashids_team = Hashids(min_length=7, salt="4fa6b775541a91c93fe92df0788d2321")
Hashids_referral = Hashids(min_length=5, salt="bbfdac22c617317cdc9ea7bc3a760188")
from Auth.utils import FirebaseAPI
from django.utils.functional import cached_property
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import now

# Create your models here.

def generate_referral_code():
    try:
        code = Hashids_referral.encode(Profile.objects.latest('id').id)
    except Profile.DoesNotExist:
        code = Hashids_referral.encode(0)
    code+=get_random_string(3, Hashids.ALPHABET)
    return code

class Event(models.Model):
    name=models.CharField(max_length=20)
    min_members=models.PositiveIntegerField(default=1)
    max_members=models.PositiveIntegerField(default=1)
    is_registration_on=models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, default = 'default')
    
    def create_team(self , profile , t_name):

        team = Team.objects.create(event=self , creator = profile,name=t_name)

        team.access_code = hashids_team.encode(team.id)
        if self.max_members==1:
            team.is_active=True
        team.save()
        member = Membership.objects.create(team=team, profile=profile)
        return team

    def __str__(self):
        return self.name 

class EventDetail(models.Model):
    title=models.CharField(max_length=50)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    content=models.TextField()
    priority=models.IntegerField()

    def __str__(self):
        return self.title + " for " + self.event.name 

class Profile(models.Model):

    GENDER_CHOICES=(
        (0,'Male'),
        (1,'Female'),
        (2,'Others/Not Specified'),
    )
    INSTITUTE_TYPE_CHOICES=(
        (0,'School'),
        (1,'College'),
        (2,'Professional'),
    )

    def get_file_path(self, filename):
        return f'media/resumes/{self.user.verified_account.uid}/{filename}'

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=128,null=True,blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    referred_by=models.ForeignKey('Profile',null=True,related_name="referred",on_delete=models.SET_NULL)
    referral_code=models.CharField(max_length=50, unique=True, default=generate_referral_code)
    institute_type = models.IntegerField(null=True, choices=INSTITUTE_TYPE_CHOICES)
    institute_name=models.CharField(max_length=128,default="")# can be school,college. last institute for professionals 
    # year , if school, implies class, undergrad&masters == yearofpassing, professional==experience
    study_year=models.PositiveIntegerField(null=True)
    # degree to be null for school
    degree=models.CharField(max_length=50,blank=True,default="")
    # to be used only by undergrad and postgrad students
    branch=models.CharField(max_length=100,blank=True,default="")
    country=models.CharField(max_length=4, default='IN')
    phone=models.CharField(max_length=15,blank=True, default="")
    gender=models.IntegerField(null=True,choices=GENDER_CHOICES)
    resume=models.FileField(upload_to=get_file_path,null=True)
    is_profile_complete=models.BooleanField(default=False)
    referral_count = models.IntegerField(default =0)
    fcm_token = models.CharField(max_length=255, null=True, blank=True)
    
    # @cached_property
    # def name(self):
    #     return f'{self.user.first_name} {self.user.last_name}'
    
    def __str__(self):
        return f'{self.name}:{self.id} from {self.institute_name}'

    def get_or_set_profile_status(self, toSet=False):
        if toSet:
            self.is_profile_complete = True
            self.save()
        profile_status = self.is_profile_complete
        if not profile_status:
            return False
        email_status = False
        try:
            email_status = self.user.verified_account.get_verified_status()
        except Exception:
            pass
        if ( profile_status and email_status):
            if (self.referred_by is not None) :
                referral,_  = ValidReferral.objects.get_or_create(by=self.referred_by, to=self)
        
        return True
        # return False
    
class ValidReferral(models.Model):
    by=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="referred_people")
    to=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name="referral")

    class Meta:
        unique_together = ('by','to')

    def __str__(self):
        return str(self.by)+" referred "+str(self.to)

class Team(models.Model):
    name=models.CharField(max_length=100)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    members=models.ManyToManyField(Profile,through='Membership',related_name="team_members")
    creator=models.ForeignKey(Profile,related_name="teams_created",on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    access_code = models.CharField(unique=True , max_length=100 , default='uninitialized')
 
    def __str__(self):          
        return self.name + " for event " + str(self.event)

    def total_members(self):
        return Membership.objects.filter(team=self).count()

    def join_team(self, profile, acc_code):
        if acc_code == self.access_code and self.total_members() < self.event.max_members:
            if self.total_members() +1 >= self.event.min_members:
                self.is_active=True
                self.save()
            
            return Membership.objects.create(team=self,profile=profile)
        
        else :
            raise(ValidationError("Maximum Size of Team reached"))

    def leave_team(self , profile):
        if profile == self.creator:
            self.delete()
            return 0
        else:
            total_members = self.total_members()
            if  total_members <= self.event.min_members:
                self.is_active=False
                self.save()

            ins  = Membership.objects.get(team=self,profile=profile)
            ins.delete()
            return total_members-1

class Membership(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)    

    class Meta:
        unique_together = ("team","profile")


    def __str__(self):
        if self.profile!=None:
            return str(self.profile)+" from team "+ str(self.team)
        return "Member ID#"+str(self.id)

class Handles(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="handles")
    codeforces = models.CharField(max_length = 100, null=True, blank=True)
    codechef = models.CharField(max_length = 100, null=True, blank=True)
    hackerrank = models.CharField(max_length = 100, null=True, blank=True)
    hackerearth = models.CharField(max_length = 100, null=True, blank=True)
    analyticsvidya = models.CharField(max_length = 100, null=True, blank=True)
    topcoder = models.CharField(max_length = 100, null=True, blank=True)
    dev_folio = models.CharField(max_length = 100, null=True, blank=True)
    
    def __str__(self):
        return f'Handles of {self.profile}'
    class Meta:
        verbose_name_plural = "Handles"


class CA(models.Model):
    caid=models.PositiveIntegerField(unique=True,null=True,blank=True)
    name = models.CharField(max_length=80)
    institute_name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    comment = models.TextField(null=True,blank=True)
    last_updated = models.DateField(default=now)
    
    def __str__(self):
        return f'{self.name} from {self.institute_name}'

@receiver(post_save, sender=ValidReferral)
def update_ref_count(sender, instance, **kwargs):
    profile = instance.by
    profile.referral_count+=1
    profile.save()