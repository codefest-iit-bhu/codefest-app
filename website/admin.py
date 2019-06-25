from django.contrib import admin
from .models import *

admin.site.register(EventDetail)
admin.site.register(ValidReferral)
admin.site.register(Membership)
admin.site.register(Handles)


class EventDetailInline(admin.TabularInline):
    model=EventDetail


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('name','is_registration_on')
    inlines=[EventDetailInline]

class MembershipInline(admin.TabularInline):
    model=Membership

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('name','event','is_active')
    inlines=(MembershipInline,)

@admin.register(CA)
class CAAdmin(admin.ModelAdmin):
    fields=('caid','name','institute_name','points','comment','last_updated')
    list_display=('caid','name', 'institute_name', 'points')
    search_fields=('caid','name','institute_name')
    ordering = ('-points',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('__str__','is_profile_complete',)
    search_fields=('user__first_name','user__username')
    list_filter=('is_profile_complete','institute_type','country')