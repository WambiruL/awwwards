from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField


from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    username=models.CharField(max_length=300,null=True)
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    location=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        print("signal activated---->>>", dir(instance))
        instance.userprofile.save

class Projects(models.Model): 
    profile = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 
    title = models.CharField(max_length=20,blank=True)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    image_landing = models.ImageField(upload_to='landing/')
    description = HTMLField(max_length=200,blank=True)
    link = URLOrRelativeURLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    @classmethod
    def search_by_projects(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        print(projects)
        return projects 
    
    @classmethod
    def get_profile_projects(cls,profile):
       projects = Projects.objects.filter(profile__pk=profile)
       print(projects)
       return projects
    
    
    def __str__(self):
        return self.title


