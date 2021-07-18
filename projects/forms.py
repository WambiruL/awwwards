from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Projects

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfleUpdateForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=['profile_image', 'bio', 'location']

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title','image_landing','description', 'link')