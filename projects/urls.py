from . import views
from django.conf.urls import url 
from projects import views as project_views
from django.contrib.auth import views as auth_views

urlpatterns=[
   
    url(r'register/', project_views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'profile/', project_views.profileView,name='profile'),
    url(r'logout/',auth_views.LogoutView.as_view(),name='logout',),
    url(r'^$',views.index,name = 'index'),
    url(r'^projects/',project_views.submit_site,name='submit_site')
   
]