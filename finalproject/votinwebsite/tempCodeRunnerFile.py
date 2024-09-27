from django.contrib import admin
from django.urls import include, path
from votinwebsite import views
app_name='votinwebsite'

urlpatterns = [

path('', views.home, name='home'),
path('login', views.login, name='login'),
path('signup', views.signup, name='signup'),
path('contact', views.contact, name='contact'),
path('result', views.result, name='result'),
path('count', views.other, name='count'),




]