from . import views
from django.conf.urls import url 
from projects import views as project_views
from django.contrib.auth import views as auth_views

urlpatterns=[
   
    url(r'register/', project_views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'profile/', project_views.profileView,name='profile'),
    url(r'^logout/',auth_views.LogoutView.as_view(),name='logout',),
    url(r'new_project/',project_views.submitSite,name='new_project'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^api/profile/$', views.UserProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.UserProfileList.as_view()),
    url(r'api/projects/projects-id/(?P<pk>[0-9]+)/$',views.ProjectsList.as_view()),

    url(r'^$',views.index,name = 'index'),
    
   
]