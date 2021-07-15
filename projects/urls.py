from . import views
from django.conf.urls import url 
from projects import views as project_views

urlpatterns=[
    url(r'register/', project_views.registerPage,name='register'),
    url(r'^$',views.index,name = 'index'),
]