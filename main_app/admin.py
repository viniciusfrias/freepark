from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Spot, Comment, Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Spot)
admin.site.register(Comment)
admin.site.register(Profile)
