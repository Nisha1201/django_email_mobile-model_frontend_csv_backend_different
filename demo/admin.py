from django.contrib import admin
from .models import Email
# Register your models here.
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display=('id','email','mobile')

# @admin.register(Moblie)
# class MobileAdmin(admin.ModelAdmin):
#     list_display=('email_id','moblie')
