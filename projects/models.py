from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    user_name=models.CharField(max_length=300,null=True)
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


