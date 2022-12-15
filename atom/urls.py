from django.urls import path

from . import views
# from views import *


urlpatterns = [
    path('index/', views.index, name='index'),
    path('',views.sun, name='sun'),
    path('check',views.check, name='check'),
    path('root',views.root, name='root'),
    path('sample',views.sample, name='sample'),
    path('method', views.method, name='method'),
    path('forms', views.forms, name='forms'),
    path('insert',views.insert, name='insert'),
    path('main',views.main, name='main'),
    path('scan',views.scan, name='scan'),

]