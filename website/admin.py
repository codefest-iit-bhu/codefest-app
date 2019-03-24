from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Institute)
admin.site.register(EventDetail)

class EventDetailInline(admin.TabularInline):
    model=EventDetail


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('name','is_registration_on')
    inlines=[EventDetailInline]