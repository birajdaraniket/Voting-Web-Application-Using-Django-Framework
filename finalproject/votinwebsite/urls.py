from django.contrib import admin
from django.urls import include, path
from votinwebsite import views
app_name='votinwebsite'

urlpatterns = [

path('', views.home, name='home'),
 path('login/', views.user_login, name='login'),

path('signup', views.sign, name='signup'),
path('contact', views.con, name='contact'),
path('result', views.res, name='result'),
path('partyregistration', views.party, name='partyregistration'),
path('index', views.index, name='index'),

path('count', views.count, name='count'),



]