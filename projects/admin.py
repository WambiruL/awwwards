from projects.models import UserProfile
from django.contrib import admin
from .models import Rates, UserProfile,Projects

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Projects)
admin.site.register(Rates)

