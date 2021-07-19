from rest_framework import serializers
from .models import UserProfile,Projects

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','profile_imae','bio') 
        
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title','image_landing','description','link')