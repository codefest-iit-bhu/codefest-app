from django.contrib import admin
from .models import VerifiedAccount
# Register your models here.
# admin.site.register(VerifiedAccount)

@admin.register(VerifiedAccount)
class VerifiedAccountAdmin(admin.ModelAdmin):
    list_display=('__str__','provider','is_verified')
    search_fields=('uid',)
    list_filter=('provider','is_verified')
    raw_id_fields=('user',)
